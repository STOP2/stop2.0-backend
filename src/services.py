import datetime
import requests
import json
import math
import io
import csv
import paho.mqtt.publish as publish
from itertools import groupby

import thread_helper

import csv
import io

class DigitransitAPIService:
    def __init__(self, db, push_notification_service, hsl_api_url):
        self.url = hsl_api_url
        self.headers = {'Content-Type': 'application/graphql'}
        self.db = db
        self.MQTT_host = "epsilon.fixme.fi"
        self.push_notification_service = push_notification_service

    def get_stops(self, lat, lon, radius):
        data = {}
        stops = []
        stop_ids = self.get_stops_near_coordinates(lat, lon, radius)

        for stop_id in stop_ids:
            stops.append({"stop": self.get_busses_by_stop_id(stop_id['stop_id'], stop_id['distance'])})

        data["stops"] = stops
        return data

    def get_stops_with_beacon(self, major, minor):
        beacons = {}
        beacon_csv = requests.get("https://dev.hsl.fi/tmp/stop_beacons.csv").text
        reader = csv.DictReader(io.StringIO(beacon_csv))
        for beacon in reader:
            beacons[(int(beacon['Major']), int(beacon['Minor']))] = beacon

        beacon = beacons.get((major, minor))
        if not beacon: # XXX unknown beacon, fake a location for now
            beacon_coords = {'lat': 60.203978, 'lon': 24.9633573}
            return self.get_stops(beacon_coords.get('lat'), beacon_coords.get('lon'), 160)
        else:
            stops = self.get_stops_by_code(beacon['Stop'])
            stop = stops['stops'][0] # XXX calculate average if multiple stops?
            return self.get_stops(stop['lat'], stop['lon'], 1)


    def get_busses_with_beacon(self, major_minor):
        result = dict()
        result['vehicles'] = []

        beacons = dict()

        csvdata = requests.get('http://dev.hsl.fi/tmp/bus_beacons.csv').text
        reader = csv.DictReader(io.StringIO(csvdata))

        for row in reader:
            beacons[(row['Major'], row['Minor'])] = row

        for mm in major_minor:
            row = beacons.get((mm['major'], mm['minor']))

            if not row:
                result['vehicles'].append(json.loads(('{"error":"Invalid major and/or minor",'
                                                    '"major":"%s",'
                                                    '"minor":"%s"}') % (mm['major'], mm['minor'])))
            else:
                if not row['Vehicle']:
                    continue
                json_data = json.loads(requests.get(('https://dev.hsl.fi/hfp/journey/bus/%s/') % (row['Vehicle'])).text)

                # The above API returns empty json object if there is not available realtime data of the bus
                if json_data == json.loads("{}"):
                    result['vehicles'].append(json.loads(('{"error":"No realtime data from the bus",'
                                                       '"major":"%s",'
                                                       '"minor":"%s"}') % (mm['major'], mm['minor'])))
                    continue

                bus = json_data[list(json_data)[0]]['VP']

                route = "HSL:" + bus['line']
                direction = int(bus['dir'])
                date = datetime.datetime.fromtimestamp(float(bus['tsi'])).strftime("%Y%m%d")
                time = math.floor( (int(bus['start'])/100) * 60) + (int(bus['start']) % 60) * 60

                data = self.fetch_single_fuzzy_trip(route, direction, date, time)

                if data is None:
                    result['vehicles'].append(json.loads(('{"error":"Invalid major and/or minor",'
                                                       '"major":"%s",'
                                                       '"minor":"%s"}') % (mm['major'], mm['minor'])))

                data['major'] = mm['major']
                data['minor'] = mm['minor']
                result['vehicles'].append(data)

        return result


    def fetch_single_fuzzy_trip(self, route, direction, date, time):
        query = ('''{fuzzyTrip(route:"%s", date:"%s", time:%d, direction:%d){
                        gtfsId
                        directionId
                        route{
                            shortName
                        }
                    }
                }''') % (route, date, time, direction)

        data = json.loads(self.get_query(query))['data']['fuzzyTrip']

        if data is None:
            return json.loads('{"error":"No trip found matching route, direction, date and time"}')

        return json.loads( ('{"trip_id":"%s", "direction":"%s", "line":"%s"}') % (data['gtfsId'], data['directionId'], data['route']['shortName']) )


    def get_stops_near_coordinates(self, lat, lon, radius):
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
                 "         stopHeadsign"
                 "         serviceDay"
                 "    	    realtimeArrival"
                 "      }"
                 "    }"
                 "  }"
                 "}") % (stop_id, datetime.datetime.now().strftime("%Y%m%d"))

        data = json.loads(self.get_query(query))["data"]["stop"]

        if data is None:
            return json.loads('{ "error":"Invalid stop id" }')

        lines = data["stoptimesForServiceDate"]

        current_time = datetime.datetime.now()

        stop = {'stop_name': data["name"], 'stop_code': data["code"], 'stop_id': stop_id, 'distance': distance, 'schedule': []}
        schedule = []
        for line in lines:
            stoptimes = line["stoptimes"]

            for time in stoptimes:
                if not "serviceDay" in time: continue

                arrival_time = datetime.datetime.fromtimestamp(time["serviceDay"] + time["realtimeArrival"])
                arrival = math.floor((arrival_time - current_time).total_seconds() / 60.0)  # Arrival in minutes
                if current_time < arrival_time and arrival < 61:
                    schedule.append({'trip_id': time["trip"]["gtfsId"],
                                     'line': line["pattern"]["route"]["shortName"],
                                     'destination': time.get("stopHeadsign", ""),
                                     'arrival': arrival,
                                     'route_id': line["pattern"]["route"]["gtfsId"],
                                     'vehicle_type': data["vehicleType"]
                                     })

        sorted_by_route = sorted(schedule, key=lambda k: k['route_id'])
        bus_list = []
        for key, group in groupby(sorted_by_route, lambda k: k['route_id']):
            group = list(group)
            group = sorted(group, key=lambda k: k['arrival'])
            group = group[:2]
            if len(group) == 2 and group[1]['arrival'] > 30:
                group.pop()
            for g in group:
                bus_list.append(g)

        bus_list = sorted(bus_list, key=lambda k: k['arrival'])
        stop["schedule"] = bus_list[:10]

        return stop

    def get_query(self, query):
        response = requests.post(self.url, data=query, headers=self.headers)

        # Force encoding as auto-detection sometimes fails
        response.encoding = 'utf-8'
        if response.text.find('"errors"') != -1:
            print("ERROR:", response.text)
        return response.text

    def make_request(self, trip_id, stop_id, device_id, push_notification):
        request_id = self.db.store_request(trip_id, stop_id, device_id, push_notification)

        data = self.get_requests(trip_id)
        publish.single(topic="stoprequests/" + trip_id, payload=json.dumps(data), hostname=self.MQTT_host, port=1883)

        result = {"request_id": request_id}
        if push_notification:
            thread_helper.start_do_every("PUSH", 30, self.notify)
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

    def store_report(self, trip_id, stop_id):
        self.db.store_report(trip_id, stop_id)

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

    def get_stops_by_trip_id(self, trip_id):
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
        data = json.loads(self.get_query(query))['data']['trip']

        if data is None:
            return json.loads('{ "error":"Invalid trip id" }')

        for stop in data['stoptimesForDate']:
            real_time = datetime.datetime.fromtimestamp(stop["serviceDay"] + stop["realtimeArrival"])
            arrival = math.floor((real_time - current_time).total_seconds() / 60.0)
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
        data = json.loads(self.get_query(query))['data']['trip']

        if data is None:
            return json.loads('{ "error":"Invalid trip id" }')

        for stop in data['stoptimesForDate']:
            if stop_id == stop['stop']['gtfsId']:
                real_time = datetime.datetime.fromtimestamp(stop["serviceDay"] + stop["realtimeArrival"])
                arrival = math.floor((real_time - current_time).total_seconds() / 60.0)
                stops.append({'stop_name': stop['stop']['name'], 'stop_code': stop['stop']['code'],
                                  'stop_id': stop['stop']['gtfsId'], 'arrives_in': arrival})
        result["stops"] = stops

        return result

    def get_stops_by_code(self, stop_code):
        query = '''{ stops(name:"%s") { gtfsId code name platformCode lat lon } }''' % stop_code
        data = json.loads(self.get_query(query))
        return data['data']

    def fetch_single_trip(self, trip_id):
        query = ('''{ trip(id:"%s"){
                        gtfsId
                        stoptimesForDate(serviceDay:"%s"){
                            serviceDay
                            realtimeArrival
                            stop{
                                gtfsId
                            }
                            }
                        }
                    }''') % (trip_id, datetime.datetime.now().strftime("%Y%m%d"))

        data = json.loads(self.get_query(query))

        return data['data']

    def notify(self):
        pushable_requests = self.fetch_pushable_requests()
        if not pushable_requests:
            thread_helper.stop_do_every("PUSH")
            return
        pushed_requests = self.fetch_trips_and_send_push_notifications(pushable_requests)
        # still need some kind of evaluation wether the notifications were sent
        if pushed_requests:
            self.db.set_pushed(pushed_requests)


    def fetch_trips_and_send_push_notifications(self, stoprequests):
        current_time = datetime.datetime.now()
        to_send = [] # List of push notifications to be sent
        pushed_requests = [] # List of ids of pushed requests

        # stoprequests is dict where:
        # stoprequests[trip_id] = [ (1_stop_id, 1_device_id), (2_stop_id, 2_device_id), ... ]
        for trip_id in stoprequests.keys():
            data = self.fetch_single_trip(trip_id)

            # In case trip_id is invalid (cancels invalid requests and send push_notifications of error)
            if data['trip'] is None:
                error_notifications = []
                for sr in stoprequests[trip_id]:
                    self.cancel_request(sr[0])
                    error_notifications.append(sr[2])
                self.push_notification_service.send_error_push_notifications(error_notifications, 'Invalid trip_id!')
                continue

            for sr in stoprequests[trip_id]:
                found = False # Whether wanted stop_id is on the route of the trip
                # sr[0] = request_id, sr[1] = stop_id, sr[2] = device_id
                for stoptime in data['trip']['stoptimesForDate']:
                    if stoptime['stop']['gtfsId'] == sr[1]:
                        found = True
                        arrival_time = datetime.datetime.fromtimestamp(stoptime['serviceDay'] + stoptime['realtimeArrival'])
                        arrival = math.floor((arrival_time - current_time).total_seconds())
                        if arrival <= 120:
                            to_send.append(sr[2])
                            pushed_requests.append(sr[0])

                # In case stop_id was invalid (cancels invalid request and send push_notification of error)
                if not found:
                    self.cancel_request(sr[0])
                    self.push_notification_service.send_error_push_notifications([sr[2]], 'Invalid stop_id!')

        if len(to_send) != 0:
            result = self.push_notification_service.send_push_notifications(to_send)
            if result[0].get('success') == 0:
                pushed_requests = []

        return pushed_requests

    def fetch_pushable_requests(self):
        pushable_requests = self.db.get_unpushed_requests()
        requests_by_trip_id = {}

        for request in pushable_requests:
            if requests_by_trip_id.get(request[0]):
                requests_by_trip_id.get(request[0]).append((request[1], request[2], request[3]))
            else:
                requests_by_trip_id[request[0]] = [(request[1], request[2], request[3])]

        return requests_by_trip_id
