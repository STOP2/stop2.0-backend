import datetime
import requests
import json
import math
import subprocess
import paho.mqtt.publish as publish
from itertools import groupby
from flask import Flask
import thread_helper


class DigitransitAPIService:
    def __init__(self, db, push_notifications, hsl_api_url):
        self.url = hsl_api_url
        self.headers = {'Content-Type': 'application/graphql'}
        self.db = db
        self.push_notifications = push_notifications
        self.MQTT_host = "epsilon.fixme.fi"
        self.all_realtime_data = None
        self.push_notification_requests = []

    def get_stops(self, lat, lon, radius=160):
        data = {}
        stops = []
        stop_ids = self.get_stops_near_coordinates(lat, lon, radius)

        for stop_id in stop_ids:
            stops.append({"stop": self.get_busses_by_stop_id(stop_id['stop_id'], stop_id['distance'])})

        data["stops"] = stops
        return data

    def get_stops_near_coordinates(self, lat, lon, radius=160):
        radius = min(radius, 1000)
        query = ("{stopsByRadius(lat:%f, lon:%f, radius:%d) {"
                 "  edges {"
                 "      node {"
                 "          distance"
                 "          stop {"
                 "    	        gtfsId"
                 "              name"
                 "              vehicleType"
                 "          }"
                 "      }"
                 "    }"
                 "  }"
                 "}") % (lat, lon, radius)
        data = json.loads(self.get_query(query))
        data = data['data']['stopsByRadius']['edges']
        stoplist = []
        for n in data:
            if n['node']['stop']['vehicleType'] == 0 or n['node']['stop']['vehicleType'] == 3:      #vehicle_type: 0 - tram, 1 - metro, 3 - bus, 4 - ferry
                stoplist.append({'stop_id': n['node']['stop']['gtfsId'], 'distance': n['node']['distance']})
        sorted(stoplist, key=lambda k: k['distance'])
        return stoplist[:3]

    def get_busses_by_stop_id(self, stop_id, distance):
        query = ("{stop(id: \"%s\") {"
                 "  name"
                 "  code"
                 "  vehicleType"
                 "  stoptimesForServiceDate(date: \"%s\"){"
                 "     pattern {"
                 "         code"
                 "         name"
                 "         directionId"
                 "         route {"
                 "             gtfsId"
                 "             longName"
                 "             shortName"
                 "         }"
                 "     }"
                 "     stoptimes {"
                 "         trip{"
                 "             gtfsId"
                 "         }"
                 "         serviceDay"
                 "    	    realtimeArrival"
                 "      }"
                 "    }"
                 "  }"
                 "}") % (stop_id, datetime.datetime.now().strftime("%Y%m%d"))

        data = json.loads(self.get_query(query))["data"]["stop"]

        lines = data["stoptimesForServiceDate"]

        current_time = datetime.datetime.now()

        stop = {'stop_name': data["name"], 'stop_code': data["code"], 'stop_id': stop_id, 'distance': distance, 'schedule': []}
        schedule = []
        for line in lines:
            stoptimes = line["stoptimes"]

            if line["pattern"]["directionId"] == 1:
                destination = line["pattern"]["route"]["longName"].split("-")[0].strip()
            else:
                destination = line["pattern"]["route"]["longName"].split("-")[-1].strip()

            for time in stoptimes:
                arrival_time = datetime.datetime.fromtimestamp(time["serviceDay"] + time["realtimeArrival"])
                arrival = math.floor((arrival_time - current_time).total_seconds() / 60.0)  # Arrival in minutes
                if current_time < arrival_time and arrival < 31:
                    schedule.append({'trip_id': time["trip"]["gtfsId"],
                                     'line': line["pattern"]["route"]["shortName"],
                                     'destination': destination,
                                     'arrival': arrival,
                                     'route_id': line["pattern"]["route"]["gtfsId"],
                                     'vehicle_type': data["vehicleType"]
                                     })

        sorted_by_route = sorted(schedule, key=lambda k: k['route_id'])
        bus_list = []
        for key, group in groupby(sorted_by_route, lambda k: k['route_id']):
            group = list(group)
            group = sorted(group, key=lambda k: k['arrival'])
            for g in group[:2]:
                bus_list.append(g)

        bus_list = sorted(bus_list, key=lambda k: k['arrival'])
        stop["schedule"] = bus_list[:10]

        return stop

    def get_query(self, query):
        response = requests.post(self.url, data=query, headers=self.headers)

        return response.text

    def make_request(self, json_data):
        request_id = self.db.store_request(json_data["trip_id"], json_data["stop_id"], json_data["device_id"])
        
        trip_id = json_data["trip_id"]
        data = self.get_requests(trip_id)
        publish.single(topic="stoprequests/" + trip_id, payload=json.dumps(data), hostname=self.MQTT_host, port=1883)

        # Add push notification request if wanted to the list and start fetching data for push notifications
        if not "push_notification" in json_data or json_data["push_notification"]:
            self.push_notification_requests.append([json_data['device_id'], json_data['stop_id'], trip_id])
            thread_helper.start_do_every('FETCHING_REALTIME_DATA', 10, self.fetch_all_realtime_json, 0)

        result = {"request_id": request_id}
        return result
    
    def get_request_info(self, request_id):
        request_data = self.db.get_request_info(request_id)
        
        query = ("{"
                 "  trip(id: \"%s\"){"
                 "      stoptimesForDate(serviceDay: \"%s\"){"
                 "          stop{"
                 "              gtfsId"
                 "              code"
                 "              name"
                 "          }"
                 "          serviceDay"
                 "          realtimeArrival"
                 "          arrivalDelay"
                 "      }"
                 "  }"
                 "}") % (request_data[0], datetime.datetime.now().strftime("%Y%m%d"))

        stop_data = json.loads(self.get_query(query))['data']['trip']['stoptimesForDate']
        result = {}
        for stop in stop_data:
            if request_data[1] == stop['stop']['gtfsId']:
                current_time = datetime.datetime.now()
                real_time = datetime.datetime.fromtimestamp(stop["serviceDay"] + stop["realtimeArrival"])
                arrival = math.floor((real_time - current_time).total_seconds() / 60.0)
                result = {'stop_name': stop['stop']['name'], 'stop_code': stop['stop']['code'],
                          'stop_id': stop['stop']['gtfsId'], 'arrives_in': arrival, 'delay': stop['arrivalDelay']}
        
        return result
        
    def cancel_request(self, request_id):
        trip_id = self.db.cancel_request(request_id)
        data = self.get_requests(trip_id)
        publish.single(topic="stoprequests/" + trip_id, payload=json.dumps(data), hostname=self.MQTT_host, port=1883)
        
        return ''
        
    def store_report(self, json_data):
        self.db.store_report(str(json_data["trip_id"]), str(json_data["stop_id"]))
        
        return ''
    
    def get_requests(self, trip_id):
        requests = self.db.get_requests(trip_id)
        stop_dict = {}
        
        for stop_id in requests:
            i = stop_dict.get(stop_id[0], 0)
            stop_dict[stop_id[0]] = i + 1
        stop_list = []
        
        for key in stop_dict.keys():
            stop_list.append({"id": key, "passengers": stop_dict[key]})
            
        return {"stop_ids": stop_list}
    
    def get_stops_by_trip_id(self, trip_id, stop_id):
        query = ("{trip(id: \"%s\") {"
                 " stoptimesForDate(serviceDay: \"%s\") {"
                 "      stop{"
                 "          gtfsId"
                 "          name"
                 "          code"
                 " }"
                 "      serviceDay"
                 "      realtimeArrival"
                 "        }"
                 "       }"
                 "      }"
                 "}") % (trip_id, datetime.datetime.now().strftime("%Y%m%d"))

        current_time = datetime.datetime.now()
        result = {}
        stops = []
        data = json.loads(self.get_query(query))['data']['trip']['stoptimesForDate']
        stop_found = False
        for stop in data:
            if stop_id == stop['stop']['gtfsId']:
                stop_found = True
            if stop_found:
                real_time = datetime.datetime.fromtimestamp(stop["serviceDay"] + stop["realtimeArrival"])
                arrival = math.floor((real_time - current_time).total_seconds() / 60.0)
                if arrival >= 0:
                    stops.append({'stop_name': stop['stop']['name'], 'stop_code': stop['stop']['code'],
                                  'stop_id': stop['stop']['gtfsId'], 'arrives_in': arrival})
        result["stops"] = stops

        return result

    def get_single_stop_by_trip_id(self, trip_id, stop_id):
        query = ("{trip(id: \"%s\") {"
                 " stoptimesForDate(serviceDay: \"%s\") {"
                 "      stop{"
                 "          gtfsId"
                 "          name"
                 "          code"
                 " }"
                 "      serviceDay"
                 "      realtimeArrival"
                 "        }"
                 "       }"
                 "      }"
                 "}") % (trip_id, datetime.datetime.now().strftime("%Y%m%d"))
    
        current_time = datetime.datetime.now()
        result = {}
        stops = []
        data = json.loads(self.get_query(query))['data']['trip']['stoptimesForDate']
        for stop in data:
            if stop_id == stop['stop']['gtfsId']:
                real_time = datetime.datetime.fromtimestamp(stop["serviceDay"] + stop["realtimeArrival"])
                arrival = math.floor((real_time - current_time).total_seconds() / 60.0)
                stops.append({'stop_name': stop['stop']['name'], 'stop_code': stop['stop']['code'],
                                  'stop_id': stop['stop']['gtfsId'], 'arrives_in': arrival})
        result["stops"] = stops
    
        return result

    #Fetches all data from "http://api.digitransit.fi/realtime/trip-updates/v1/HSL" as JSON and saves it as self.all_realtime_data
    def fetch_all_realtime_json(self):
        #Gets realtime data from API, converts it to JSON and saves it to 'json.txt'
        subprocess.call(Flask(__name__).root_path + "/./gtfs_realtime_json \"http://api.digitransit.fi/realtime/trip-updates/v1/HSL\" > json.txt", shell=True)
        #Reads the text file and saves it as string
        with open('json.txt', 'r') as file:
            data = file.read().strip()

        self.all_realtime_data = json.loads(data)

        self.send_push_notifications()


    def send_push_notifications(self):
        to_send = []

        for r in self.push_notification_requests:
            for entity in self.all_realtime_data['entity']:
                trip_update = entity['trip_update']

                try:
                    if len(trip_update) <= 4 and len(trip_update['stop_time_update']) == 1:
                        if ( r[1] == trip_update['stop_time_update'][1]['stop_id'] and
                                trip_update['trip']['route_id'] in r[2] and
                                trip_update['trip']['start_date'] in r[2] and
                                trip_update['trip']['start_time'].replace(':', '')[:-2] in r[2]):
                                    # Add device id saved in r[0] to list of pussh notifications to send
                                    to_send.append(r[0])
                                    # Delete push notification request
                                    self.push_notification_requests.remove(r)
                except:
                    pass

        # Send push notifications if there are any
        if not len(to_send) == 0:
            self.push_notifications.send_push_notification(to_send)
        # Stop running fetch_all_realtime_json if self.push_notification_requests is empty
        if len(self.push_notification_requests) == 0:
            thread_helper.stop_do_every('FETCHING_REALTIME_DATA')


    def start_fetching_realtime_data_test(self):
        thread_helper.start_do_every('FETCHING_REALTIME_DATA', 10, self.fetch_all_realtime_json, 10)

    def force_stop_fetching_realtime_data(self):
        thread_helper.stop_do_every('FETCHING_REALTIME_DATA')

    def get_all_realtime_data(self):
        return json.dumps(self.all_realtime_data)
