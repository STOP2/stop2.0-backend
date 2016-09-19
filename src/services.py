import datetime
import requests
import json
import math


class DigitransitAPIService:
    def __init__(self):
        self.url = 'http://api.digitransit.fi/routing/v1/routers/hsl/index/graphql'
        #datetime.datetime.now().strftime("%Y%m%d")


    def get_stops_near_cordinates(self, lat, lon, radius=20):
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
        data = json.loads(self.getQuery(query))
        data = data['data']['stopsByRadius']['edges']
        stoplist = []
        for n in data:
            stoplist.append(n['node']['stop']['gtfsId'])
        return stoplist

    def get_stops(self, x, y):
        data = {}
        stopsData = []
        #stops = self.get_stops_near_coordinates(x, y)

        #for stop in stops:
        #    stopsData.append(self.get_busses_by_stop_id(stop.id)["data"])

        stop = json.loads(self.get_busses_by_stop_id("HSL:1362141"))
        stopsData.append(stop["data"])
        data["stops"] = stopsData

        return data


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
            stoptimes = line["stoptimes"]
            for time in stoptimes:
                arrival_time = datetime.datetime.fromtimestamp(time["serviceDay"] + time["realtimeArrival"])
                arrival = math.floor((arrival_time - current_time).total_seconds() / 60.0)  #Arrival in minutes
                if current_time < arrival_time:
                    schedule.append({'bus_id': line["pattern"]["id"],
                                     'line': line["pattern"]["route"]["shortName"],
                                     'destination': line["pattern"]["route"]["longName"],
                                     'arrival': arrival,
                                     'routeId': line["pattern"]["route"]["gtfsId"],
                                     'direction': line["pattern"]["directionId"]})

        sorted_list = sorted(schedule, key=lambda k: k['arrival'])
        stop["schedule"] = sorted_list

        return stop

    def getQuery(self, url, query, headers):
        response = requests.post(url, data=query, headers=headers)

        return response.text
