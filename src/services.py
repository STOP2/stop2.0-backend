import datetime
import requests
import json
import math
import paho.mqtt.publish as publish


class DigitransitAPIService:
    def __init__(self, db):
        self.url = 'http://api.digitransit.fi/routing/v1/routers/hsl/index/graphql'
        self.headers = {'Content-Type': 'application/graphql'}
        self.db = db
        self.MQTT_host = "epsilon.fixme.fi"

    def get_stops(self, lat, lon, radius=160):
        data = {}
        stops = []
        stop_ids = self.get_stops_near_coordinates(lat, lon, radius)

        for stop_id in stop_ids:
            stops.append({"stop": self.get_busses_by_stop_id(stop_id)})

        data["stops"] = stops
        return data

    def get_stops_near_coordinates(self, lat, lon, radius=160):
        if radius > 1000:
            radius = 1000

        query = ("{stopsByRadius(lat:%f, lon:%f, radius:%d) {"
                 "  edges {"
                 "      node {"
                 "          distance"
                 "          stop {"
                 "    	        gtfsId"
                 "              name"
                 "          }"
                 "      }"
                 "    }"
                 "  }"
                 "}") % (lat, lon, radius)
        data = json.loads(self.get_query(query))
        data = data['data']['stopsByRadius']['edges']
        stoplist = []
        for n in data:
            stoplist.append(n['node']['stop']['gtfsId'])
        return stoplist[:3]

    def get_busses_by_stop_id(self, stop_id):
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

        data = {}
        data = json.loads(self.get_query(query))["data"]["stop"]

        lines = data["stoptimesForServiceDate"]

        current_time = datetime.datetime.now()

        stop = {'stop_name': data["name"], 'stop_code': data["code"], 'schedule': []}
        schedule = []
        for line in lines:
            stoptimes = line["stoptimes"]

            if line["pattern"]["directionId"] == 1:
                destination = line["pattern"]["route"]["longName"].split("-")[0].strip()
            else:
                destination = line["pattern"]["route"]["longName"].split("-")[-1].strip()

            for time in stoptimes:
                arrival_time = datetime.datetime.fromtimestamp(time["serviceDay"] + time["realtimeArrival"])
                if current_time < arrival_time:
                    arrival = math.floor((arrival_time - current_time).total_seconds() / 60.0)  # Arrival in minutes
                    schedule.append({'trip_id': time["trip"]["gtfsId"][4:],
                                     'line': line["pattern"]["route"]["shortName"],
                                     'destination': destination,
                                     'arrival': arrival,
                                     'route_id': line["pattern"]["route"]["gtfsId"],
                                     'vehicle_type': data["vehicleType"]
                                     })
        sorted_list = sorted(schedule, key=lambda k: k['arrival'])
        stop["schedule"] = sorted_list[:10]

        return stop

    def get_query(self, query):
        response = requests.post(self.url, data=query, headers=self.headers)

        return response.text

    def make_request(self, jsonData):
        self.db.store_request(jsonData["trip_id"], jsonData["stop_id"])
        bus_id = jsonData["trip_id"]
        del jsonData["trip_id"]
        jsonData = json.dumps(jsonData)
        publish.single(topic="stoprequests/" + bus_id, payload=jsonData, hostname=self.MQTT_host, port=1883)
        return ''

    def get_stops_by_trip_id(self, trip_id):
        query = ("{trip(id:\"%s\") {"
                     "   gtfsId"
                     "   pattern {"
                     "       stops {"
                     "           gtfsId"
                     "           code"
                     "           name"
                     "        }"
                     "       }"
                     "      }"
                     "}") % (trip_id)
        result = {}
        stops = []
        data = json.loads(self.get_query(query))['data']['trip']['pattern']['stops']
        for stop in data:
            stops.append({'stop_id': stop['gtfsId'], 'stop_code': stop['code'], 'stop_name': stop['name']})
        result["stops"] = stops
        return result