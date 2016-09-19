import datetime
import requests
import json
import math
import re

class DigitransitAPIService:
    def __init__(self):
        self.url = 'http://api.digitransit.fi/routing/v1/routers/hsl/index/graphql'
        #datetime.datetime.now().strftime("%Y%m%d")

    def get_stops(self):
        return ''

    def get_stops_near_coordinates(self):
        return ''

    def get_busses_by_stop_id(self, stop_id):
        url = 'http://api.digitransit.fi/routing/v1/routers/hsl/index/graphql'
        headers = {'Content-Type': 'application/graphql'}
        query =  ("{stop(id: \"%s\") {"
                      "  name"
                      "  code"
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

        data = json.loads(self.getQuery(url, query, headers))["data"]["stop"]

        lines = data["stoptimesForServiceDate"]

        current_time = datetime.datetime.now()

        stop = {'stop_name': data["name"], 'stop_code': data["code"], 'schedule': []}
        schedule = []
        for line in lines:
            destination = line["pattern"]["route"]["longName"]

            stoptimes = line["stoptimes"]
            for time in stoptimes:
                arrival_time = datetime.datetime.fromtimestamp(time["serviceDay"] + time["realtimeArrival"])
                arrival = math.floor((arrival_time - current_time).total_seconds() / 60.0)
                if current_time < arrival_time:
                    schedule.append({'line': line["pattern"]["route"]["shortName"],
                                     'destination': destination,
                                     'arrival': arrival,
                                     'routeId': line["pattern"]["route"]["gtfsId"],
                                     'direction': line["pattern"]["directionId"]})

        sorted_list = sorted(schedule, key=lambda k: k['arrival'])
        stop["schedule"] = sorted_list

        return stop

    def getQuery(self, url, query, headers):
        response = requests.post(url, data=query, headers=headers)

        return response.text