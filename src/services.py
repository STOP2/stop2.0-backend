import datetime
import requests
import json

class DigitransitAPIService:
    def __init__(self):
        self.url = 'http://api.digitransit.fi/routing/v1/routers/hsl/index/graphql'
        #datetime.datetime.now().strftime("%Y%m%d")

    def get_stops(self):
        return ''

    def get_stops_near_coordinates(self):
        return ''

    def get_busses_by_stop_id(self, stop_id):
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
                      "             shortName"
                      "         }"
                      "     }"
                      "     stoptimes {"
                      "         serviceDay"
                      "      	scheduledArrival"
                      "    	    realtimeArrival"
                      "      }"
                      "    }"
                      "  }"
                      "}") % (stop_id, datetime.datetime.now().strftime("%Y%m%d"))

        return self.getQuery(query)

    def getQuery(self, query):
        headers = {'Content-Type': 'application/graphql'}
        response = requests.post(self.url, data=query, headers=headers)

        return response.text