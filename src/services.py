import datetime
import requests
import json
import math


class DigitransitAPIService:
    def __init__(self):
        self.url = 'http://api.digitransit.fi/routing/v1/routers/hsl/index/graphql'
        self.headers = {'Content-Type': 'application/graphql'}

    def get_stops(self, lat, lon, radius=160):
        data = {}
        stops = []
        stop_ids = self.get_stops_near_coordinates(lat, lon, radius)

        for stop_id in stop_ids:
            stops.append({"stop": self.get_busses_by_stop_id(stop_id)})

        data["stops"] = stops
        return data

    def get_stops_near_coordinates(self, lat, lon, radius=160):
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
        return stoplist

    def get_busses_by_stop_id(self, stop_id):
        query = ("{stop(id: \"%s\") {"
                      "  name"
                      "  code"
                      "  vehicleType"
                      "  stoptimesForServiceDate(date: \"%s\"){"
                      "     pattern {"
                      "         id"
                      "         name"
                      "         directionId"
                      "         route {"
                      "             gtfsId"
                      "             longName"
                      "             shortName"
                      "         }"
                      "     }"
                      "     stoptimes {"
                      "         serviceDay"
                      "    	    realtimeArrival"
                      "      }"
                      "    }"
                      "  }"
                      "}") % (stop_id, datetime.datetime.now().strftime("%Y%m%d"))

        data = json.loads(self.get_query(query))["data"]["stop"]

        lines = data["stoptimesForServiceDate"]

        current_time = datetime.datetime.now()

        stop = {'stop_name': data["name"], 'stop_code': data["code"], 'schedule': []}
        schedule = []
        for line in lines:
            stoptimes = line["stoptimes"]

            if line["pattern"]["directionId"]==1:
                destination = line["pattern"]["route"]["longName"].split("-")[0].strip()
            else:
                destination = line["pattern"]["route"]["longName"].split("-")[-1].strip()

            for time in stoptimes:
                arrival_time = datetime.datetime.fromtimestamp(time["serviceDay"] + time["realtimeArrival"])
                arrival = math.floor((arrival_time - current_time).total_seconds() / 60.0)  # Arrival in minutes
                if current_time < arrival_time:
                    schedule.append({'vehicle_id': line["pattern"]["id"],
                                     'line': line["pattern"]["route"]["shortName"],
                                     'destination': destination,
                                     'arrival': arrival,
                                     'routeId': line["pattern"]["route"]["gtfsId"],
                                     'vehicle_type': data["vehicleType"]
                                     })

        sorted_list = sorted(schedule, key=lambda k: k['arrival'])
        stop["schedule"] = sorted_list[:10]

        return stop

    def get_query(self, query):
        response = requests.post(self.url, data=query, headers=self.headers)

        return response.text
