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

        return self.getQuery(url, query, headers)

    def getQuery(self, url, query, headers):
        response = requests.post(url, data=query, headers=headers)

        return response.text