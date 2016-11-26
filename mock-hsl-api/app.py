# coding=utf-8
import datetime
import re
import time
from flask import Flask
from flask import request
from waitress import serve

app = Flask(__name__)


@app.route('/', methods=['POST'])
def mock():
    request_body = request.data.decode('utf-8')
    
    if request_body == '{stopsByRadius(lat:60.203978, lon:24.963357, radius:300) {  edges {      node {          distance          stop {    	        gtfsId              name              vehicleType          }      }    }  }}':
        return '''
{
  "data": {
    "stop": {
      "vehicleType": 3,
      "stoptimesForServiceDate": [
        {
          "pattern": {
            "name": "717A to Sotungin koulu (HSL:4940201)",
            "route": {
              "longName": "Rautatientori-Jakomäki-Hakunila-Sotunki",
              "shortName": "717A",
              "gtfsId": "HSL:4717A"
            },
            "directionId": 0,
            "code": "HSL:4717A:0:01"
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161114_La_1_1455"
              },
              "realtimeArrival": 54780,
              "stopHeadsign": "Sotunki via Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161114_La_1_1555"
              },
              "realtimeArrival": 58440,
              "stopHeadsign": "Sotunki via Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161114_La_1_1655"
              },
              "realtimeArrival": 62040,
              "stopHeadsign": "Sotunki via Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161114_La_1_1755"
              },
              "realtimeArrival": 65580,
              "stopHeadsign": "Sotunki via Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161114_La_1_1855"
              },
              "realtimeArrival": 69180,
              "stopHeadsign": "Sotunki via Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161114_La_1_1955"
              },
              "realtimeArrival": 72780,
              "stopHeadsign": "Sotunki via Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161114_La_1_1055"
              },
              "realtimeArrival": 40260,
              "stopHeadsign": "Sotunki via Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161114_La_1_1155"
              },
              "realtimeArrival": 43920,
              "stopHeadsign": "Sotunki via Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161114_La_1_1255"
              },
              "realtimeArrival": 47580,
              "stopHeadsign": "Sotunki via Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161114_La_1_1355"
              },
              "realtimeArrival": 51180,
              "stopHeadsign": "Sotunki via Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161114_La_1_0955"
              },
              "realtimeArrival": 36660,
              "stopHeadsign": "Sotunki via Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161114_La_1_0755"
              },
              "realtimeArrival": 29400,
              "stopHeadsign": "Sotunki via Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161114_La_1_0855"
              },
              "realtimeArrival": 33060,
              "stopHeadsign": "Sotunki via Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161114_La_1_2055"
              },
              "realtimeArrival": 76380,
              "stopHeadsign": "Sotunki via Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161114_La_1_2155"
              },
              "realtimeArrival": 79800,
              "stopHeadsign": "Sotunki via Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161114_La_1_2310"
              },
              "realtimeArrival": 84300,
              "stopHeadsign": "Sotunki via Hakunila",
              "serviceDay": 1480111200
            }
          ]
        },
        {
          "pattern": {
            "name": "739V to Siikatie (HSL:4860247) from Rautatientori (HSL:1020115) via Sipoontie (HSL:4860208)",
            "route": {
              "longName": "Rautatientori-Päiväkumpu-Pohjois-Nikinmäki",
              "shortName": "739V",
              "gtfsId": "HSL:4739V"
            },
            "directionId": 0,
            "code": "HSL:4739V:0:01"
          },
          "stoptimes": []
        },
        {
          "pattern": {
            "name": "739V to Siikatie (HSL:4860247) from Rautatientori (HSL:1020115) via Täkytie (HSL:4860252)",
            "route": {
              "longName": "Rautatientori-Päiväkumpu-Pohjois-Nikinmäki",
              "shortName": "739V",
              "gtfsId": "HSL:4739V"
            },
            "directionId": 0,
            "code": "HSL:4739V:0:02"
          },
          "stoptimes": []
        },
        {
          "pattern": {
            "name": "787K to Pornainen Shell (HSL:9400201)",
            "route": {
              "longName": "Rautatientori-Kuninkaanmäki-Nikkilä-Pornainen",
              "shortName": "787K",
              "gtfsId": "HSL:9787K"
            },
            "directionId": 0,
            "code": "HSL:9787K:0:01"
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:9787K_20161114_La_1_1240"
              },
              "realtimeArrival": 46560,
              "stopHeadsign": "Pornainen via Nikkilä",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:9787K_20161114_La_1_1640"
              },
              "realtimeArrival": 60960,
              "stopHeadsign": "Pornainen via Nikkilä",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:9787K_20161114_La_1_2040"
              },
              "realtimeArrival": 75360,
              "stopHeadsign": "Pornainen via Nikkilä",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:9787K_20161114_La_1_2515"
              },
              "realtimeArrival": 91680,
              "stopHeadsign": "Pornainen via Nikkilä",
              "serviceDay": 1480111200
            }
          ]
        },
        {
          "pattern": {
            "name": "718 to Nissas (HSL:4940229)",
            "route": {
              "longName": "Rautatientori-Nissas",
              "shortName": "718",
              "gtfsId": "HSL:4718"
            },
            "directionId": 0,
            "code": "HSL:4718:0:01"
          },
          "stoptimes": []
        },
        {
          "pattern": {
            "name": "717N to Kuninkaanmäki (HSL:4970233)",
            "route": {
              "longName": "Rautatientori-Jakomäki-Hakunila-Kuninkaanmäki",
              "shortName": "717N",
              "gtfsId": "HSL:4717N"
            },
            "directionId": 0,
            "code": "HSL:4717N:0:01"
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:4717N_20161114_La_1_2740"
              },
              "realtimeArrival": 100500,
              "stopHeadsign": "Kuninkaanmäki via Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717N_20161114_La_1_2810"
              },
              "realtimeArrival": 102300,
              "stopHeadsign": "Kuninkaanmäki via Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717N_20161114_La_1_2610"
              },
              "realtimeArrival": 95100,
              "stopHeadsign": "Kuninkaanmäki via Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717N_20161114_La_1_2640"
              },
              "realtimeArrival": 96900,
              "stopHeadsign": "Kuninkaanmäki via Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717N_20161114_La_1_2710"
              },
              "realtimeArrival": 98700,
              "stopHeadsign": "Kuninkaanmäki via Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717N_20161114_La_1_2340"
              },
              "realtimeArrival": 86160,
              "stopHeadsign": "Kuninkaanmäki via Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717N_20161114_La_1_2510"
              },
              "realtimeArrival": 91440,
              "stopHeadsign": "Kuninkaanmäki via Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717N_20161114_La_1_2540"
              },
              "realtimeArrival": 93240,
              "stopHeadsign": "Kuninkaanmäki via Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717N_20161114_La_1_2410"
              },
              "realtimeArrival": 87900,
              "stopHeadsign": "Kuninkaanmäki via Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717N_20161114_La_1_2440"
              },
              "realtimeArrival": 89640,
              "stopHeadsign": "Kuninkaanmäki via Hakunila",
              "serviceDay": 1480111200
            }
          ]
        },
        {
          "pattern": {
            "name": "731N to Laulurastaantie (HSL:4810216)",
            "route": {
              "longName": "Rautatientori-Kulomäki",
              "shortName": "731N",
              "gtfsId": "HSL:4731N"
            },
            "directionId": 0,
            "code": "HSL:4731N:0:01"
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:4731N_20161114_La_1_1935"
              },
              "realtimeArrival": 71520,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731N_20161114_La_1_1905"
              },
              "realtimeArrival": 69780,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731N_20161114_La_1_2238"
              },
              "realtimeArrival": 82440,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731N_20161114_La_1_2105"
              },
              "realtimeArrival": 76860,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731N_20161114_La_1_2137"
              },
              "realtimeArrival": 78780,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731N_20161114_La_1_2442"
              },
              "realtimeArrival": 89820,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731N_20161114_La_1_2340"
              },
              "realtimeArrival": 86160,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731N_20161114_La_1_2642"
              },
              "realtimeArrival": 97080,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731N_20161114_La_1_2542"
              },
              "realtimeArrival": 93480,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731N_20161114_La_1_2842"
              },
              "realtimeArrival": 104100,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731N_20161114_La_1_2742"
              },
              "realtimeArrival": 100620,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731N_20161114_La_1_2035"
              },
              "realtimeArrival": 75060,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731N_20161114_La_1_2005"
              },
              "realtimeArrival": 73260,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731N_20161114_La_1_0730"
              },
              "realtimeArrival": 27900,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731N_20161114_La_1_0640"
              },
              "realtimeArrival": 24780,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731N_20161114_La_1_0540"
              },
              "realtimeArrival": 21120,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            }
          ]
        },
        {
          "pattern": {
            "name": "786",
            "route": {
              "longName": "Rautatientori-Jokivarsi-Nikkilä-Järvenpään asema",
              "shortName": "786",
              "gtfsId": "HSL:9786"
            },
            "directionId": 0,
            "code": "HSL:9786:0:01"
          },
          "stoptimes": []
        },
        {
          "pattern": {
            "name": "717 to Kuninkaanmäki (HSL:4970233)",
            "route": {
              "longName": "Rautatientori-Jakomäki-Hakunila-Kuninkaanmäki",
              "shortName": "717",
              "gtfsId": "HSL:4717"
            },
            "directionId": 0,
            "code": "HSL:4717:0:01"
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_2035"
              },
              "realtimeArrival": 75180,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_2015"
              },
              "realtimeArrival": 73980,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_2135"
              },
              "realtimeArrival": 78660,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_2115"
              },
              "realtimeArrival": 77460,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_2215"
              },
              "realtimeArrival": 81000,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_2240"
              },
              "realtimeArrival": 82500,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_1015"
              },
              "realtimeArrival": 37860,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_1035"
              },
              "realtimeArrival": 39060,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_1135"
              },
              "realtimeArrival": 42720,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_1115"
              },
              "realtimeArrival": 41520,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_1215"
              },
              "realtimeArrival": 45120,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_1235"
              },
              "realtimeArrival": 46320,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_1335"
              },
              "realtimeArrival": 49980,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_1315"
              },
              "realtimeArrival": 48780,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_1415"
              },
              "realtimeArrival": 52380,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_1435"
              },
              "realtimeArrival": 53580,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_1535"
              },
              "realtimeArrival": 57240,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_1515"
              },
              "realtimeArrival": 56040,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_1635"
              },
              "realtimeArrival": 60840,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_1615"
              },
              "realtimeArrival": 59640,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_1735"
              },
              "realtimeArrival": 64380,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_1715"
              },
              "realtimeArrival": 63240,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_1815"
              },
              "realtimeArrival": 66780,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_1835"
              },
              "realtimeArrival": 67980,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_1915"
              },
              "realtimeArrival": 70380,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_1935"
              },
              "realtimeArrival": 71580,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_0645"
              },
              "realtimeArrival": 25080,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_0725"
              },
              "realtimeArrival": 27600,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_0825"
              },
              "realtimeArrival": 31260,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_0915"
              },
              "realtimeArrival": 34260,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161114_La_1_0935"
              },
              "realtimeArrival": 35460,
              "stopHeadsign": "Kuninkaanmäki via  Hakunila",
              "serviceDay": 1480111200
            }
          ]
        },
        {
          "pattern": {
            "name": "848 to Linja-autoasema (HSL:9300204)",
            "route": {
              "longName": "Kamppi-Pasila-Viikki-Söderkulla-Porvoo",
              "shortName": "848",
              "gtfsId": "HSL:7848"
            },
            "directionId": 0,
            "code": "HSL:7848:0:01"
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:7848_20161114_La_1_0918"
              },
              "realtimeArrival": 34500,
              "stopHeadsign": "Porvoo via Söderkulla",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161114_La_1_1618"
              },
              "realtimeArrival": 59700,
              "stopHeadsign": "Porvoo via Söderkulla",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161114_La_1_1518"
              },
              "realtimeArrival": 56100,
              "stopHeadsign": "Porvoo via Söderkulla",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161114_La_1_1918"
              },
              "realtimeArrival": 70500,
              "stopHeadsign": "Porvoo via Söderkulla",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161114_La_1_1718"
              },
              "realtimeArrival": 63300,
              "stopHeadsign": "Porvoo via Söderkulla",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161114_La_1_1818"
              },
              "realtimeArrival": 66900,
              "stopHeadsign": "Porvoo via Söderkulla",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161114_La_1_1218"
              },
              "realtimeArrival": 45300,
              "stopHeadsign": "Porvoo via Söderkulla",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161114_La_1_1118"
              },
              "realtimeArrival": 41700,
              "stopHeadsign": "Porvoo via Söderkulla",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161114_La_1_1418"
              },
              "realtimeArrival": 52500,
              "stopHeadsign": "Porvoo via Söderkulla",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161114_La_1_1318"
              },
              "realtimeArrival": 48900,
              "stopHeadsign": "Porvoo via Söderkulla",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161114_La_1_1018"
              },
              "realtimeArrival": 38100,
              "stopHeadsign": "Porvoo via Söderkulla",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161114_La_1_2518"
              },
              "realtimeArrival": 92100,
              "stopHeadsign": "Porvoo via Söderkulla",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161114_La_1_2418"
              },
              "realtimeArrival": 88500,
              "stopHeadsign": "Porvoo via Söderkulla",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161114_La_1_2718"
              },
              "realtimeArrival": 99300,
              "stopHeadsign": "Porvoo via Söderkulla",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161114_La_1_2618"
              },
              "realtimeArrival": 95700,
              "stopHeadsign": "Porvoo via Söderkulla",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161114_La_1_2118"
              },
              "realtimeArrival": 77700,
              "stopHeadsign": "Porvoo via Söderkulla",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161114_La_1_2018"
              },
              "realtimeArrival": 74100,
              "stopHeadsign": "Porvoo via Söderkulla",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161114_La_1_2318"
              },
              "realtimeArrival": 84900,
              "stopHeadsign": "Porvoo via Söderkulla",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161114_La_1_2218"
              },
              "realtimeArrival": 81300,
              "stopHeadsign": "Porvoo via Söderkulla",
              "serviceDay": 1480111200
            }
          ]
        },
        {
          "pattern": {
            "name": "518 to Kuninkaanmäki (HSL:4970233)",
            "route": {
              "longName": "Ilmala-Pasila-Kuninkaanmäki",
              "shortName": "518",
              "gtfsId": "HSL:4518"
            },
            "directionId": 0,
            "code": "HSL:4518:0:01"
          },
          "stoptimes": []
        },
        {
          "pattern": {
            "name": "738 to Jukolantien kp. (HSL:5000246)",
            "route": {
              "longName": "Rautatientori-Kerava",
              "shortName": "738",
              "gtfsId": "HSL:9738"
            },
            "directionId": 0,
            "code": "HSL:9738:0:01"
          },
          "stoptimes": []
        },
        {
          "pattern": {
            "name": "724 to Päiväkummuntie (HSL:4750222)",
            "route": {
              "longName": "Rautatientori-Jokiniemi-Päiväkumpu",
              "shortName": "724",
              "gtfsId": "HSL:4724"
            },
            "directionId": 0,
            "code": "HSL:4724:0:01"
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:4724_20161114_La_1_0825"
              },
              "realtimeArrival": 31260,
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161114_La_1_0725"
              },
              "realtimeArrival": 27540,
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161114_La_1_0925"
              },
              "realtimeArrival": 34920,
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161114_La_1_1125"
              },
              "realtimeArrival": 42120,
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161114_La_1_1025"
              },
              "realtimeArrival": 38520,
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161114_La_1_1325"
              },
              "realtimeArrival": 49320,
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161114_La_1_1225"
              },
              "realtimeArrival": 45720,
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161114_La_1_1925"
              },
              "realtimeArrival": 70980,
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161114_La_1_1825"
              },
              "realtimeArrival": 67440,
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161114_La_1_1525"
              },
              "realtimeArrival": 56580,
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161114_La_1_1425"
              },
              "realtimeArrival": 52980,
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161114_La_1_1725"
              },
              "realtimeArrival": 63840,
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161114_La_1_1625"
              },
              "realtimeArrival": 60180,
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161114_La_1_2313"
              },
              "realtimeArrival": 84540,
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161114_La_1_2025"
              },
              "realtimeArrival": 74580,
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161114_La_1_2213"
              },
              "realtimeArrival": 80940,
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161114_La_1_2125"
              },
              "realtimeArrival": 78060,
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1480111200
            }
          ]
        },
        {
          "pattern": {
            "name": "788 to Linja-autoasema (HSL:9300201)",
            "route": {
              "longName": "Rautatientori-Jokivarsi-Nikkilä-Hinthaara-Porvoo",
              "shortName": "788",
              "gtfsId": "HSL:9788"
            },
            "directionId": 0,
            "code": "HSL:9788:0:01"
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:9788_20161114_La_1_1040"
              },
              "realtimeArrival": 39360,
              "stopHeadsign": "Porvoo via Nikkilä",
              "serviceDay": 1480111200
            }
          ]
        },
        {
          "pattern": {
            "name": "785K to Nikkilän la-as. (HSL:9222202)",
            "route": {
              "longName": "Rautatientori-Kuninkaanmäki-Nikkilä",
              "shortName": "785K",
              "gtfsId": "HSL:9785K"
            },
            "directionId": 0,
            "code": "HSL:9785K:0:01"
          },
          "stoptimes": []
        },
        {
          "pattern": {
            "name": "787 to Pornainen Shell (HSL:9400201)",
            "route": {
              "longName": "Rautatientori-Jokivarsi-Nikkilä-Pornainen",
              "shortName": "787",
              "gtfsId": "HSL:9787"
            },
            "directionId": 0,
            "code": "HSL:9787:0:01"
          },
          "stoptimes": []
        },
        {
          "pattern": {
            "name": "787A to Halkia (HSL:9400204) from Rautatientori (HSL:1020120) express",
            "route": {
              "longName": "Rautatientori-Jokivarsi-Nikkilä-Pornainen-Halkia",
              "shortName": "787A",
              "gtfsId": "HSL:9787A"
            },
            "directionId": 0,
            "code": "HSL:9787A:0:02"
          },
          "stoptimes": []
        },
        {
          "pattern": {
            "name": "787A to Halkia (HSL:9400204) from Rautatientori (HSL:1020120) via Laukkoski (HSL:9400205)",
            "route": {
              "longName": "Rautatientori-Jokivarsi-Nikkilä-Pornainen-Halkia",
              "shortName": "787A",
              "gtfsId": "HSL:9787A"
            },
            "directionId": 0,
            "code": "HSL:9787A:0:01"
          },
          "stoptimes": []
        },
        {
          "pattern": {
            "name": "731 to Laulurastaantie (HSL:4810216)",
            "route": {
              "longName": "Rautatientori-Kulomäki",
              "shortName": "731",
              "gtfsId": "HSL:4731"
            },
            "directionId": 0,
            "code": "HSL:4731:0:01"
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:4731_20161114_La_1_1837"
              },
              "realtimeArrival": 68040,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161114_La_1_1807"
              },
              "realtimeArrival": 66300,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161114_La_1_1637"
              },
              "realtimeArrival": 60960,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161114_La_1_1737"
              },
              "realtimeArrival": 64560,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161114_La_1_1707"
              },
              "realtimeArrival": 62760,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161114_La_1_1537"
              },
              "realtimeArrival": 57300,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161114_La_1_1607"
              },
              "realtimeArrival": 59160,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161114_La_1_1437"
              },
              "realtimeArrival": 53700,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161114_La_1_1407"
              },
              "realtimeArrival": 51900,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161114_La_1_1507"
              },
              "realtimeArrival": 55500,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161114_La_1_1337"
              },
              "realtimeArrival": 50100,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161114_La_1_1307"
              },
              "realtimeArrival": 48240,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161114_La_1_1237"
              },
              "realtimeArrival": 46440,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161114_La_1_1207"
              },
              "realtimeArrival": 44640,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161114_La_1_1137"
              },
              "realtimeArrival": 42840,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161114_La_1_1107"
              },
              "realtimeArrival": 41040,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161114_La_1_1040"
              },
              "realtimeArrival": 39420,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161114_La_1_1010"
              },
              "realtimeArrival": 37620,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161114_La_1_0940"
              },
              "realtimeArrival": 35820,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161114_La_1_0910"
              },
              "realtimeArrival": 34020,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161114_La_1_0840"
              },
              "realtimeArrival": 32220,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161114_La_1_0810"
              },
              "realtimeArrival": 30420,
              "stopHeadsign": "Kulomäki via Korso",
              "serviceDay": 1480111200
            }
          ]
        },
        {
          "pattern": {
            "name": "738K to Jukolantien kp. (HSL:5000246)",
            "route": {
              "longName": "Rautatientori-Kerava",
              "shortName": "738K",
              "gtfsId": "HSL:9738K"
            },
            "directionId": 0,
            "code": "HSL:9738K:0:01"
          },
          "stoptimes": []
        },
        {
          "pattern": {
            "name": "788K to Linja-autoasema (HSL:9300201)",
            "route": {
              "longName": "Rautatientori-Kuninkaanmäki-Nikkilä-Hinthaara-Porvoo",
              "shortName": "788K",
              "gtfsId": "HSL:9788K"
            },
            "directionId": 0,
            "code": "HSL:9788K:0:01"
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:9788K_20161114_La_1_1840"
              },
              "realtimeArrival": 68160,
              "stopHeadsign": "Porvoo via Nikkilä",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:9788K_20161114_La_1_1440"
              },
              "realtimeArrival": 53760,
              "stopHeadsign": "Porvoo via Nikkilä",
              "serviceDay": 1480111200
            }
          ]
        },
        {
          "pattern": {
            "name": "77 to Kalteentie (HSL:1414149)",
            "route": {
              "longName": "Rautatientori-Jakomäki",
              "shortName": "77",
              "gtfsId": "HSL:1077"
            },
            "directionId": 0,
            "code": "HSL:1077:0:01"
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_2006"
              },
              "realtimeArrival": 73380,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_2026"
              },
              "realtimeArrival": 74580,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_2046"
              },
              "realtimeArrival": 75780,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_2126"
              },
              "realtimeArrival": 78120,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_2146"
              },
              "realtimeArrival": 79320,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_2106"
              },
              "realtimeArrival": 76920,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_2253"
              },
              "realtimeArrival": 83340,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_2207"
              },
              "realtimeArrival": 80580,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_2227"
              },
              "realtimeArrival": -1,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_2323"
              },
              "realtimeArrival": 85140,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1226"
              },
              "realtimeArrival": 45780,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1246"
              },
              "realtimeArrival": 47040,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1206"
              },
              "realtimeArrival": 44580,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1346"
              },
              "realtimeArrival": 50700,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1306"
              },
              "realtimeArrival": 48240,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1326"
              },
              "realtimeArrival": 49440,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1426"
              },
              "realtimeArrival": 53100,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1446"
              },
              "realtimeArrival": 54300,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1406"
              },
              "realtimeArrival": 51900,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1546"
              },
              "realtimeArrival": 57900,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1506"
              },
              "realtimeArrival": 55500,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1526"
              },
              "realtimeArrival": 56700,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1606"
              },
              "realtimeArrival": 59100,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1626"
              },
              "realtimeArrival": 60300,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1646"
              },
              "realtimeArrival": 61500,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1706"
              },
              "realtimeArrival": 62700,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1726"
              },
              "realtimeArrival": 63900,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1746"
              },
              "realtimeArrival": 65100,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1826"
              },
              "realtimeArrival": 67440,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1846"
              },
              "realtimeArrival": 68640,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1806"
              },
              "realtimeArrival": 66240,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1946"
              },
              "realtimeArrival": 72240,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1906"
              },
              "realtimeArrival": 69840,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1926"
              },
              "realtimeArrival": 71040,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1027"
              },
              "realtimeArrival": 38580,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1047"
              },
              "realtimeArrival": 39780,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1007"
              },
              "realtimeArrival": 37380,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1147"
              },
              "realtimeArrival": 43440,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1107"
              },
              "realtimeArrival": 41040,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_1127"
              },
              "realtimeArrival": 42240,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_0735"
              },
              "realtimeArrival": 28140,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_0705"
              },
              "realtimeArrival": 26340,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_0835"
              },
              "realtimeArrival": 31800,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_0805"
              },
              "realtimeArrival": 30000,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_0947"
              },
              "realtimeArrival": 36180,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_0907"
              },
              "realtimeArrival": 33720,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_0927"
              },
              "realtimeArrival": 34920,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_0635"
              },
              "realtimeArrival": 24420,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161114_La_1_0605"
              },
              "realtimeArrival": 22620,
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1480111200
            }
          ]
        },
        {
          "pattern": {
            "name": "788KV",
            "route": {
              "longName": "Rautatientori-Kuninkaanmäki-Nikkilä-Hinthaara-Porvoo",
              "shortName": "788KV",
              "gtfsId": "HSL:9788KV"
            },
            "directionId": 0,
            "code": "HSL:9788KV:0:01"
          },
          "stoptimes": []
        },
        {
          "pattern": {
            "name": "739 to Siikatie (HSL:4860247)",
            "route": {
              "longName": "Rautatientori-Päiväkumpu-Korso-Pohjois-Nikinmäki",
              "shortName": "739",
              "gtfsId": "HSL:4739"
            },
            "directionId": 0,
            "code": "HSL:4739:0:01"
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:4739_20161114_La_1_1043"
              },
              "realtimeArrival": 39600,
              "stopHeadsign": "Pohjois-Nikinmäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161114_La_1_1143"
              },
              "realtimeArrival": 43200,
              "stopHeadsign": "Pohjois-Nikinmäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161114_La_1_1943"
              },
              "realtimeArrival": 72000,
              "stopHeadsign": "Pohjois-Nikinmäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161114_La_1_1743"
              },
              "realtimeArrival": 64860,
              "stopHeadsign": "Pohjois-Nikinmäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161114_La_1_1843"
              },
              "realtimeArrival": 68460,
              "stopHeadsign": "Pohjois-Nikinmäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161114_La_1_1543"
              },
              "realtimeArrival": 57600,
              "stopHeadsign": "Pohjois-Nikinmäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161114_La_1_1643"
              },
              "realtimeArrival": 61260,
              "stopHeadsign": "Pohjois-Nikinmäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161114_La_1_1343"
              },
              "realtimeArrival": 50400,
              "stopHeadsign": "Pohjois-Nikinmäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161114_La_1_1243"
              },
              "realtimeArrival": 46800,
              "stopHeadsign": "Pohjois-Nikinmäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161114_La_1_1443"
              },
              "realtimeArrival": 54000,
              "stopHeadsign": "Pohjois-Nikinmäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161114_La_1_0851"
              },
              "realtimeArrival": 32880,
              "stopHeadsign": "Pohjois-Nikinmäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161114_La_1_0944"
              },
              "realtimeArrival": 36060,
              "stopHeadsign": "Pohjois-Nikinmäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161114_La_1_0651"
              },
              "realtimeArrival": 25560,
              "stopHeadsign": "Pohjois-Nikinmäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161114_La_1_0751"
              },
              "realtimeArrival": 29160,
              "stopHeadsign": "Pohjois-Nikinmäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161114_La_1_2354"
              },
              "realtimeArrival": 87000,
              "stopHeadsign": "Pohjois-Nikinmäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161114_La_1_2454"
              },
              "realtimeArrival": 90540,
              "stopHeadsign": "Pohjois-Nikinmäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161114_La_1_2151"
              },
              "realtimeArrival": 79620,
              "stopHeadsign": "Pohjois-Nikinmäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161114_La_1_2251"
              },
              "realtimeArrival": 83220,
              "stopHeadsign": "Pohjois-Nikinmäki via Korso",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161114_La_1_2051"
              },
              "realtimeArrival": 76020,
              "stopHeadsign": "Pohjois-Nikinmäki via Korso",
              "serviceDay": 1480111200
            }
          ]
        },
        {
          "pattern": {
            "name": "724N to Päiväkummuntie (HSL:4750222)",
            "route": {
              "longName": "Rautatientori-Tikkurila-Koivukylä-Päiväkumpu",
              "shortName": "724N",
              "gtfsId": "HSL:4724N"
            },
            "directionId": 0,
            "code": "HSL:4724N:0:01"
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:4724N_20161114_La_1_2805"
              },
              "realtimeArrival": 101940,
              "stopHeadsign": "Päiväkumpu via Tikkurila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4724N_20161114_La_1_2505"
              },
              "realtimeArrival": 91140,
              "stopHeadsign": "Päiväkumpu via Tikkurila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4724N_20161114_La_1_2405"
              },
              "realtimeArrival": 87540,
              "stopHeadsign": "Päiväkumpu via Tikkurila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4724N_20161114_La_1_2705"
              },
              "realtimeArrival": 98340,
              "stopHeadsign": "Päiväkumpu via Tikkurila",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4724N_20161114_La_1_2605"
              },
              "realtimeArrival": 94740,
              "stopHeadsign": "Päiväkumpu via Tikkurila",
              "serviceDay": 1480111200
            }
          ]
        },
        {
          "pattern": {
            "name": "722 to Halmekuja (HSL:4740233)",
            "route": {
              "longName": "Rautatientori-Honkanummi-Havukoski",
              "shortName": "722",
              "gtfsId": "HSL:4722"
            },
            "directionId": 0,
            "code": "HSL:4722:0:01"
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:4722_20161114_La_1_1700"
              },
              "realtimeArrival": 62280,
              "stopHeadsign": "Havukoski",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161114_La_1_1800"
              },
              "realtimeArrival": 65820,
              "stopHeadsign": "Havukoski",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161114_La_1_1900"
              },
              "realtimeArrival": 69420,
              "stopHeadsign": "Havukoski",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161114_La_1_1500"
              },
              "realtimeArrival": 55080,
              "stopHeadsign": "Havukoski",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161114_La_1_1600"
              },
              "realtimeArrival": 58680,
              "stopHeadsign": "Havukoski",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161114_La_1_1300"
              },
              "realtimeArrival": 47820,
              "stopHeadsign": "Havukoski",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161114_La_1_1400"
              },
              "realtimeArrival": 51420,
              "stopHeadsign": "Havukoski",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161114_La_1_1100"
              },
              "realtimeArrival": 40620,
              "stopHeadsign": "Havukoski",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161114_La_1_1200"
              },
              "realtimeArrival": 44220,
              "stopHeadsign": "Havukoski",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161114_La_1_1000"
              },
              "realtimeArrival": 36960,
              "stopHeadsign": "Havukoski",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161114_La_1_0900"
              },
              "realtimeArrival": 33360,
              "stopHeadsign": "Havukoski",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161114_La_1_0620"
              },
              "realtimeArrival": 23640,
              "stopHeadsign": "Havukoski",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161114_La_1_0520"
              },
              "realtimeArrival": 20040,
              "stopHeadsign": "Havukoski",
              "serviceDay": 1480111200
            }
          ]
        },
        {
          "pattern": {
            "name": "785 to Nikkilän la-as. (HSL:9222202)",
            "route": {
              "longName": "Rautatientori-Jokivarsi-Nikkilä",
              "shortName": "785",
              "gtfsId": "HSL:9785"
            },
            "directionId": 0,
            "code": "HSL:9785:0:01"
          },
          "stoptimes": []
        }
      ],
      "name": "Viikki",
      "code": "3035"
    }
  }
}
                '''
    
    elif request_body == '{stopsByRadius(lat:60.203978, lon:24.963357, radius:160) {  edges {      node {          distance          stop {    	        gtfsId              name              vehicleType          }      }    }  }}':
        return '''
{
  "data": {
    "stopsByRadius": {
      "edges": [
        {
          "node": {
            "distance": 158,
            "stop": {
              "gtfsId": "HSL:1240133",
              "name": "A.I. Virtasen aukio",
              "vehicleType": 3
            }
          }
        },
        {
          "node": {
            "distance": 160,
            "stop": {
              "gtfsId": "MATKA:2_1240133",
              "name": "A.I. Virtasen aukio",
              "vehicleType": -999
            }
          }
        }
      ]
    }
  }
}
        '''
    
    elif request_body == '{stopsByRadius(lat:60.203978, lon:24.963357, radius:10) {  edges {      node {          distance          stop {    	        gtfsId              name              vehicleType          }      }    }  }}':
        return '''
{
  "data": {
    "stopsByRadius": {
      "edges": []
    }
  }
}
        '''

    elif request_body == '{stop(id: "HSL:1362141") {  name  code  vehicleType  stoptimesForServiceDate(date: "%s"){     pattern {         code         name         directionId         route {             gtfsId             longName             shortName         }     }     stoptimes {         trip{             gtfsId         }         stopHeadsign         serviceDay    	    realtimeArrival      }    }  }}' % (datetime.datetime.now().strftime("%Y%m%d")):
        return re.sub(r'"serviceDay":.*,',
                      '"serviceDay": ' + str(int(time.mktime(time.strptime(datetime.datetime.now().strftime("%Y%m%d"), "%Y%m%d")))) + ",",
            '''
        {
  "data": {
    "stop": {
      "name": "Viikki",
      "code": "3035",
      "vehicleType": 3,
      "stoptimesForServiceDate": [
        {
          "pattern": {
            "code": "HSL:4718:0:01",
            "name": "718 to Nissas (HSL:4940229)",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:4718",
              "longName": "Rautatientori - Nissas",
              "shortName": "718"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1524"
              },
              "stopHeadsign": "Nissas",
              "realtimeArrival": 56820
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1509"
              },
              "stopHeadsign": "Nissas",
              "serviceDay": 1478556000,
              "realtimeArrival": 55860
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1554"
              },
              "stopHeadsign": "Nissas",
              "serviceDay": 1478556000,
              "realtimeArrival": 58620
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1539"
              },
              "stopHeadsign": "Nissas",
              "serviceDay": 1478556000,
              "realtimeArrival": 57720
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1639"
              },
              "stopHeadsign": "Nissas",
              "serviceDay": 1478556000,
              "realtimeArrival": 61260
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1624"
              },
              "stopHeadsign": "Nissas",
              "serviceDay": 1478556000,
              "realtimeArrival": 60420
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1609"
              },
              "stopHeadsign": "Nissas",
              "serviceDay": 1478556000,
              "realtimeArrival": 59520
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1654"
              },
              "stopHeadsign": "Nissas",
              "serviceDay": 1478556000,
              "realtimeArrival": 62160
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1454"
              },
              "stopHeadsign": "Nissas",
              "serviceDay": 1478556000,
              "realtimeArrival": 54960
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1906"
              },
              "stopHeadsign": "Nissas",
              "serviceDay": 1478556000,
              "realtimeArrival": 69900
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1946"
              },
              "stopHeadsign": "Nissas",
              "serviceDay": 1478556000,
              "realtimeArrival": 72300
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1926"
              },
              "stopHeadsign": "Nissas",
              "serviceDay": 1478556000,
              "realtimeArrival": 71100
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1746"
              },
              "stopHeadsign": "Nissas",
              "serviceDay": 1478556000,
              "realtimeArrival": 65160
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1726"
              },
              "stopHeadsign": "Nissas",
              "serviceDay": 1478556000,
              "realtimeArrival": 63960
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1709"
              },
              "stopHeadsign": "Nissas",
              "serviceDay": 1478556000,
              "realtimeArrival": 63000
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1846"
              },
              "stopHeadsign": "Nissas",
              "serviceDay": 1478556000,
              "realtimeArrival": 68760
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1826"
              },
              "stopHeadsign": "Nissas",
              "serviceDay": 1478556000,
              "realtimeArrival": 67560
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1806"
              },
              "stopHeadsign": "Nissas",
              "serviceDay": 1478556000,
              "realtimeArrival": 66360
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:4722:0:01",
            "name": "722 to Halmekuja (HSL:4740233)",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:4722",
              "longName": "Rautatientori - Honkanummi - Havukoski",
              "shortName": "722"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_0520"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 20100
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_0550"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 21900
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_0620"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 23880
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_0649"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 25620
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_0738"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 28620
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_0715"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 27240
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_0850"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 32940
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_0800"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 29940
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_0820"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 31140
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1000"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 37140
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1100"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 40740
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1200"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 44340
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1300"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 48000
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1350"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 51000
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1442"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 54180
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1502"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 55440
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1520"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 56520
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1542"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 57900
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1600"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 58980
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1620"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 60180
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1635"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 61020
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1655"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 62160
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1725"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 63840
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1800"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 65940
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1900"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 69480
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_2100"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 76680
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_2000"
              },
              "stopHeadsign": "Havukoski",
              "serviceDay": 1478556000,
              "realtimeArrival": 73080
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:4717A:0:01",
            "name": "717A to Sotungin koulu (HSL:4940201)",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:4717A",
              "longName": "Rautatientori - Jakomäki - Hakunila - Sotunki",
              "shortName": "717A"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1400"
              },
              "stopHeadsign": "Sotunki",
              "serviceDay": 1478556000,
              "realtimeArrival": 51540
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1430"
              },
              "stopHeadsign": "Sotunki",
              "serviceDay": 1478556000,
              "realtimeArrival": 53400
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1530"
              },
              "stopHeadsign": "Sotunki",
              "serviceDay": 1478556000,
              "realtimeArrival": 57180
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1500"
              },
              "stopHeadsign": "Sotunki",
              "serviceDay": 1478556000,
              "realtimeArrival": 55200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1630"
              },
              "stopHeadsign": "Sotunki",
              "serviceDay": 1478556000,
              "realtimeArrival": 60720
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1600"
              },
              "stopHeadsign": "Sotunki",
              "serviceDay": 1478556000,
              "realtimeArrival": 58980
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1755"
              },
              "stopHeadsign": "Sotunki",
              "serviceDay": 1478556000,
              "realtimeArrival": 65640
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1700"
              },
              "stopHeadsign": "Sotunki",
              "serviceDay": 1478556000,
              "realtimeArrival": 62400
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1055"
              },
              "stopHeadsign": "Sotunki",
              "serviceDay": 1478556000,
              "realtimeArrival": 40380
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1155"
              },
              "stopHeadsign": "Sotunki",
              "serviceDay": 1478556000,
              "realtimeArrival": 44040
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1300"
              },
              "stopHeadsign": "Sotunki",
              "serviceDay": 1478556000,
              "realtimeArrival": 47940
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1330"
              },
              "stopHeadsign": "Sotunki",
              "serviceDay": 1478556000,
              "realtimeArrival": 49740
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1855"
              },
              "stopHeadsign": "Sotunki",
              "serviceDay": 1478556000,
              "realtimeArrival": 69180
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1955"
              },
              "stopHeadsign": "Sotunki",
              "serviceDay": 1478556000,
              "realtimeArrival": 72780
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_0955"
              },
              "stopHeadsign": "Sotunki",
              "serviceDay": 1478556000,
              "realtimeArrival": 36780
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_0600"
              },
              "stopHeadsign": "Sotunki",
              "serviceDay": 1478556000,
              "realtimeArrival": 22500
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_0630"
              },
              "stopHeadsign": "Sotunki",
              "serviceDay": 1478556000,
              "realtimeArrival": 24420
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_0730"
              },
              "stopHeadsign": "Sotunki",
              "serviceDay": 1478556000,
              "realtimeArrival": 28140
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_0700"
              },
              "stopHeadsign": "Sotunki",
              "serviceDay": 1478556000,
              "realtimeArrival": 26280
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_0800"
              },
              "stopHeadsign": "Sotunki",
              "serviceDay": 1478556000,
              "realtimeArrival": 29940
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_0855"
              },
              "stopHeadsign": "Sotunki",
              "serviceDay": 1478556000,
              "realtimeArrival": 33180
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_2310"
              },
              "stopHeadsign": "Sotunki",
              "serviceDay": 1478556000,
              "realtimeArrival": 84360
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_2155"
              },
              "stopHeadsign": "Sotunki",
              "serviceDay": 1478556000,
              "realtimeArrival": 79860
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_2055"
              },
              "stopHeadsign": "Sotunki",
              "serviceDay": 1478556000,
              "realtimeArrival": 76380
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:4739:0:01",
            "name": "739 to Siikatie (HSL:4860247)",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:4739",
              "longName": "Rautatientori - Päiväkumpu - Korso - Pohjois-Nikinmäki",
              "shortName": "739"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_2144"
              },
              "stopHeadsign": "Pohjois-Nikinmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 79260
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_2042"
              },
              "stopHeadsign": "Pohjois-Nikinmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 75600
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_2351"
              },
              "stopHeadsign": "Pohjois-Nikinmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 86760
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_2251"
              },
              "stopHeadsign": "Pohjois-Nikinmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 83220
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1042"
              },
              "stopHeadsign": "Pohjois-Nikinmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 39660
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1242"
              },
              "stopHeadsign": "Pohjois-Nikinmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 46860
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1142"
              },
              "stopHeadsign": "Pohjois-Nikinmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 43260
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1400"
              },
              "stopHeadsign": "Pohjois-Nikinmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 51540
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1428"
              },
              "stopHeadsign": "Pohjois-Nikinmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 53280
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1330"
              },
              "stopHeadsign": "Pohjois-Nikinmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 49740
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1600"
              },
              "stopHeadsign": "Pohjois-Nikinmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 58980
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1630"
              },
              "stopHeadsign": "Pohjois-Nikinmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 60780
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1500"
              },
              "stopHeadsign": "Pohjois-Nikinmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 55320
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1530"
              },
              "stopHeadsign": "Pohjois-Nikinmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 57180
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1844"
              },
              "stopHeadsign": "Pohjois-Nikinmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 68520
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1700"
              },
              "stopHeadsign": "Pohjois-Nikinmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 62520
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1730"
              },
              "stopHeadsign": "Pohjois-Nikinmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 64200
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1800"
              },
              "stopHeadsign": "Pohjois-Nikinmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 65880
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1942"
              },
              "stopHeadsign": "Pohjois-Nikinmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 72000
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_0535"
              },
              "stopHeadsign": "Pohjois-Nikinmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 20940
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_0730"
              },
              "stopHeadsign": "Pohjois-Nikinmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 28200
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_0800"
              },
              "stopHeadsign": "Pohjois-Nikinmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 30000
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_0630"
              },
              "stopHeadsign": "Pohjois-Nikinmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 24420
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_0700"
              },
              "stopHeadsign": "Pohjois-Nikinmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 26340
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_0842"
              },
              "stopHeadsign": "Pohjois-Nikinmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 32460
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_0942"
              },
              "stopHeadsign": "Pohjois-Nikinmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 36060
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:9787A:0:02",
            "name": "787A to Halkia (HSL:9400204) from Rautatientori (HSL:1020120) express",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:9787A",
              "longName": "Rautatientori - Jokivarsi - Nikkilä - Pornainen - Halkia",
              "shortName": "787A"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:9787A_20161022_Ti_1_1830"
              },
              "stopHeadsign": "Halkia",
              "serviceDay": 1478556000,
              "realtimeArrival": 67620
            },
            {
              "trip": {
                "gtfsId": "HSL:9787A_20161022_Ti_1_1615"
              },
              "stopHeadsign": "Halkia",
              "serviceDay": 1478556000,
              "realtimeArrival": 59640
            },
            {
              "trip": {
                "gtfsId": "HSL:9787A_20161022_Ti_1_2000"
              },
              "stopHeadsign": "Halkia",
              "serviceDay": 1478556000,
              "realtimeArrival": 72960
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:9787A:0:01",
            "name": "787A to Halkia (HSL:9400204) from Rautatientori (HSL:1020120) via Laukkoski (HSL:9400205)",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:9787A",
              "longName": "Rautatientori - Jokivarsi - Nikkilä - Pornainen - Halkia",
              "shortName": "787A"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:9787A3_20161022_Ti_1_1010"
              },
              "stopHeadsign": "Halkia",
              "serviceDay": 1478556000,
              "realtimeArrival": 37560
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:4717:0:01",
            "name": "717 to Kuninkaanmäki (HSL:4970233)",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:4717",
              "longName": "Rautatientori - Jakomäki - Hakunila - Kuninkaanmäki",
              "shortName": "717"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1915"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 70380
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1935"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 71580
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1515"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 56220
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1445"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 54300
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1415"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 52500
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1615"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 59880
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1545"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 58080
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1715"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 63300
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1735"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 64440
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1645"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 61500
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1835"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 67980
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1815"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 66780
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1015"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 37980
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1035"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 39180
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1135"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 42780
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1115"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 41580
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1215"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 45240
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1235"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 46440
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1345"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 50640
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1315"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 48840
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_2015"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 73980
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_2035"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 75180
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_2135"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 78660
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_2115"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 77580
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_2215"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 81060
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_2240"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 82560
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_0645"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 25320
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_0615"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 23400
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_0715"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 27240
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_0745"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 29040
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_0835"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 31980
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_0815"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 30840
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_0915"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 34380
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_0935"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 35580
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_0520"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 19980
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_0540"
              },
              "stopHeadsign": "Kuninkaanmäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 21240
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:4724:0:01",
            "name": "724 to Päiväkummuntie (HSL:4750222)",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:4724",
              "longName": "Rautatientori - Jokiniemi - Päiväkumpu",
              "shortName": "724"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1025"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 38580
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1125"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 42240
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1225"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 45840
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1325"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 49440
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1425"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 53040
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1925"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 70980
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1450"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 54720
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1510"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 55920
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1550"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 58440
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1528"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 57120
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1610"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 59640
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1640"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 61320
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1740"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 64740
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1710"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 63000
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1848"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 68760
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1820"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 67080
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_2315"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 84660
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_2025"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 74580
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_2125"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 78120
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_2215"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 81120
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_0635"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 24720
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_0605"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 22800
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_0735"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 28440
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_0705"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 26580
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_0805"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 30300
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_0835"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 32040
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_0926"
              },
              "stopHeadsign": "Päiväkumpu",
              "serviceDay": 1478556000,
              "realtimeArrival": 35100
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:1077:0:01",
            "name": "77 to Kalteentie (HSL:1414149)",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:1077",
              "longName": "Rautatientori - Jakomäki",
              "shortName": "77"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1614"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 59820
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1604"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 59280
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1634"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 60960
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1624"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 60360
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1654"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 62160
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1644"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 61560
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1716"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 63420
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1704"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 62700
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1738"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 64680
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1727"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 64020
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1758"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 65820
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1748"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 65280
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1809"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 66480
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1825"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 67440
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1845"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 68640
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1925"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 71040
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1945"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 72180
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1905"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 69840
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_2006"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 73440
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_2026"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 74580
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_2046"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 75780
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_2207"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 80580
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_2106"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 76980
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_2126"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 78180
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_2146"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 79320
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_2323"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 85080
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_2227"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 81780
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_2253"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 83280
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0721"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 27600
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0711"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 26940
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0741"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 28860
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0731"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 28260
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0751"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 29460
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0844"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 32580
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0831"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 31860
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0801"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 30060
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0821"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 31260
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0811"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 30660
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0904"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 33780
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0924"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 34980
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0944"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 36180
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0553"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 22020
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0613"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 23340
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0633"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 24600
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0653"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 25860
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1204"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 44580
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1224"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 45780
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1124"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 42372
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1144"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 43380
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1304"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 48240
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1339"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 50340
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1324"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 49440
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1354"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 51240
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1244"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 46980
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1409"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 52140
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1439"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 54000
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1424"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 53040
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1454"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 54960
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1514"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 56160
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1504"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 55560
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1534"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 57480
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1524"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 56820
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1554"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 58680
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1544"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 58080
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1104"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 40980
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1004"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 37380
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1024"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 38580
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1044"
              },
              "stopHeadsign": "Jakomäki",
              "serviceDay": 1478556000,
              "realtimeArrival": 39780
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:4717N:0:01",
            "name": "717N to Kuninkaanmäki (HSL:4970233)",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:4717N",
              "longName": "Rautatientori - Jakomäki - Hakunila - Kuninkaanmäki",
              "shortName": "717N"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:4717N_20161017_Ti_1_2610"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 95040
            },
            {
              "trip": {
                "gtfsId": "HSL:4717N_20161017_Ti_1_2340"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 86160
            },
            {
              "trip": {
                "gtfsId": "HSL:4717N_20161017_Ti_1_2540"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 93180
            },
            {
              "trip": {
                "gtfsId": "HSL:4717N_20161017_Ti_1_2510"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 91380
            },
            {
              "trip": {
                "gtfsId": "HSL:4717N_20161017_Ti_1_2440"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 89640
            },
            {
              "trip": {
                "gtfsId": "HSL:4717N_20161017_Ti_1_2410"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 87900
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:9788:0:01",
            "name": "788 to Linja-autoasema (HSL:9300201)",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:9788",
              "longName": "Rautatientori - Jokivarsi - Nikkilä - Hinthaara - Porvoo",
              "shortName": "788"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:9788_20161022_Ti_1_0615"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 23400
            },
            {
              "trip": {
                "gtfsId": "HSL:9788_20161022_Ti_1_0725"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 27660
            },
            {
              "trip": {
                "gtfsId": "HSL:9788_20161022_Ti_1_1900"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 69360
            },
            {
              "trip": {
                "gtfsId": "HSL:9788_20161022_Ti_1_1555"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 58440
            },
            {
              "trip": {
                "gtfsId": "HSL:9788_20161022_Ti_1_1500"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 55140
            },
            {
              "trip": {
                "gtfsId": "HSL:9788_20161022_Ti_1_1400"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 51420
            },
            {
              "trip": {
                "gtfsId": "HSL:9788_20161022_Ti_1_1730"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 64080
            },
            {
              "trip": {
                "gtfsId": "HSL:9788_20161022_Ti_1_1630"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 60540
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:9738K:0:01",
            "name": "738K to Jukolantien kp. (HSL:5000246)",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:9738K",
              "longName": "Rautatientori - Kerava",
              "shortName": "738K"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:9738K_20161017_Ti_1_0459"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 18780
            },
            {
              "trip": {
                "gtfsId": "HSL:9738K_20161017_Ti_1_0643"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 25260
            },
            {
              "trip": {
                "gtfsId": "HSL:9738K_20161017_Ti_1_1253"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 47520
            },
            {
              "trip": {
                "gtfsId": "HSL:9738K_20161017_Ti_1_1535"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 57420
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:9785:0:01",
            "name": "785 to Nikkilän la-as. (HSL:9222202)",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:9785",
              "longName": "Rautatientori - Jokivarsi - Nikkilä",
              "shortName": "785"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:9785_20161022_Ti_1_1750"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 65280
            },
            {
              "trip": {
                "gtfsId": "HSL:9785_20161022_Ti_1_1540"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 57540
            },
            {
              "trip": {
                "gtfsId": "HSL:9785_20161022_Ti_1_0830"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 31560
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:4731N:0:01",
            "name": "731N to Laulurastaantie (HSL:4810216)",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:4731N",
              "longName": "Rautatientori - Kulomäki",
              "shortName": "731N"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:4731N_20161024_Ti_1_2238"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 82500
            },
            {
              "trip": {
                "gtfsId": "HSL:4731N_20161024_Ti_1_2340"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 86100
            },
            {
              "trip": {
                "gtfsId": "HSL:4731N_20161024_Ti_1_2442"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 89700
            },
            {
              "trip": {
                "gtfsId": "HSL:4731N_20161024_Ti_1_2542"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 93300
            },
            {
              "trip": {
                "gtfsId": "HSL:4731N_20161024_Ti_1_2135"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 78780
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:4739V:0:01",
            "name": "739V to Siikatie (HSL:4860247) from Rautatientori (HSL:1020115) via Sipoontie (HSL:4860208)",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:4739V",
              "longName": "Rautatientori - Päiväkumpu - Pohjois-Nikinmäki",
              "shortName": "739V"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:4739V_20161024_Ti_1_1130"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 42540
            },
            {
              "trip": {
                "gtfsId": "HSL:4739V_20161024_Ti_1_1513"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 56160
            },
            {
              "trip": {
                "gtfsId": "HSL:4739V_20161024_Ti_1_1644"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 61560
            },
            {
              "trip": {
                "gtfsId": "HSL:4739V_20161024_Ti_1_1744"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 64980
            },
            {
              "trip": {
                "gtfsId": "HSL:4739V_20161024_Ti_1_1905"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 69780
            },
            {
              "trip": {
                "gtfsId": "HSL:4739V_20161024_Ti_1_2005"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 73380
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:4739V:0:02",
            "name": "739V to Siikatie (HSL:4860247) from Rautatientori (HSL:1020115) via Täkytie (HSL:4860252)",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:4739V",
              "longName": "Rautatientori - Päiväkumpu - Pohjois-Nikinmäki",
              "shortName": "739V"
            }
          },
          "stoptimes": []
        },
        {
          "pattern": {
            "code": "HSL:9787K:0:01",
            "name": "787K to Pornainen Shell (HSL:9400201)",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:9787K",
              "longName": "Rautatientori - Kuninkaanmäki - Nikkilä - Pornainen",
              "shortName": "787K"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:9787K_20161022_Ti_1_1315"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 48720
            },
            {
              "trip": {
                "gtfsId": "HSL:9787K_20161022_Ti_1_0655"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 25860
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:9786:0:01",
            "name": "786",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:9786",
              "longName": "Rautatientori - Jokivarsi - Nikkilä - Järvenpään asema",
              "shortName": "786"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:9786_20161022_Ti_1_1645"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 61380
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:9785K:0:01",
            "name": "785K to Nikkilän la-as. (HSL:9222202)",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:9785K",
              "longName": "Rautatientori - Kuninkaanmäki - Nikkilä",
              "shortName": "785K"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:9785K_20161022_Ti_1_1810"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 66420
            },
            {
              "trip": {
                "gtfsId": "HSL:9785K_20161022_Ti_1_1710"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 62880
            },
            {
              "trip": {
                "gtfsId": "HSL:9785K_20161022_Ti_1_1605"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 59100
            },
            {
              "trip": {
                "gtfsId": "HSL:9785K_20161022_Ti_1_1425"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 52920
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:9738:0:01",
            "name": "738 to Jukolantien kp. (HSL:5000246)",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:9738",
              "longName": "Rautatientori - Kerava",
              "shortName": "738"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:9738_20161017_Ti_1_1651"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 61920
            },
            {
              "trip": {
                "gtfsId": "HSL:9738_20161017_Ti_1_1619"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 60060
            },
            {
              "trip": {
                "gtfsId": "HSL:9738_20161017_Ti_1_1518"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 56400
            },
            {
              "trip": {
                "gtfsId": "HSL:9738_20161017_Ti_1_1425"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 53040
            },
            {
              "trip": {
                "gtfsId": "HSL:9738_20161017_Ti_1_1454"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 54900
            },
            {
              "trip": {
                "gtfsId": "HSL:9738_20161017_Ti_1_1756"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 65700
            },
            {
              "trip": {
                "gtfsId": "HSL:9738_20161017_Ti_1_1731"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 64260
            },
            {
              "trip": {
                "gtfsId": "HSL:9738_20161017_Ti_1_0750"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 29400
            },
            {
              "trip": {
                "gtfsId": "HSL:9738_20161017_Ti_1_0855"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 33180
            },
            {
              "trip": {
                "gtfsId": "HSL:9738_20161017_Ti_1_0816"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 30960
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:9788K:0:01",
            "name": "788K to Linja-autoasema (HSL:9300201)",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:9788K",
              "longName": "Rautatientori - Kuninkaanmäki - Nikkilä - Hinthaara - Porvoo",
              "shortName": "788K"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:9788K_20161022_Ti_1_1215"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 45060
            },
            {
              "trip": {
                "gtfsId": "HSL:9788K_20161022_Ti_1_0900"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 33360
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:4724N:0:01",
            "name": "724N to Päiväkummuntie (HSL:4750222)",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:4724N",
              "longName": "Rautatientori - Tikkurila - Koivukylä - Päiväkumpu",
              "shortName": "724N"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:4724N_20161024_Ti_1_2505"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 91080
            },
            {
              "trip": {
                "gtfsId": "HSL:4724N_20161024_Ti_1_2405"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 87540
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:7848:0:01",
            "name": "848 to Linja-autoasema (HSL:9300204)",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:7848",
              "longName": "Kamppi - Pasila - Viikki - Söderkulla - Porvoo",
              "shortName": "848"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:7848_20161101_Ti_1_2518"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 92100
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161101_Ti_1_2418"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 88500
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161101_Ti_1_1018"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 38220
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161101_Ti_1_0918"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 34620
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161101_Ti_1_0848"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 32820
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161101_Ti_1_0818"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 31020
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161101_Ti_1_0718"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 27420
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161101_Ti_1_0748"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 29220
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161101_Ti_1_0638"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 25020
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161101_Ti_1_2318"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 84900
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161101_Ti_1_2218"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 81300
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161101_Ti_1_2118"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 77700
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161101_Ti_1_2018"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 74100
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161101_Ti_1_1818"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 66900
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161101_Ti_1_1748"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 65220
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161101_Ti_1_1718"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 63420
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161101_Ti_1_1648"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 61620
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161101_Ti_1_1618"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 59820
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161101_Ti_1_1548"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 58020
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161101_Ti_1_1518"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 56220
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161101_Ti_1_1418"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 52620
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161101_Ti_1_1448"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 54420
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161101_Ti_1_1318"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 49020
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161101_Ti_1_1218"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 45420
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161101_Ti_1_1118"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 41820
            },
            {
              "trip": {
                "gtfsId": "HSL:7848_20161101_Ti_1_1918"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 70500
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:9787:0:01",
            "name": "787 to Pornainen Shell (HSL:9400201)",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:9787",
              "longName": "Rautatientori - Jokivarsi - Nikkilä - Pornainen",
              "shortName": "787"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:9787_20161022_Ti_1_1700"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 62280
            },
            {
              "trip": {
                "gtfsId": "HSL:9787_20161022_Ti_1_1520"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 56340
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:4731:0:01",
            "name": "731 to Laulurastaantie (HSL:4810216)",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:4731",
              "longName": "Rautatientori - Kulomäki",
              "shortName": "731"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_0610"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 23100
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_0630"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 24420
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_0655"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 25980
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_0550"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 21840
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_0834"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 31980
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_0854"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 33180
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_0814"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 30780
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_0714"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 27180
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_0734"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 28380
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_0754"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 29580
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_0954"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 36720
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_0914"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 34380
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_0934"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 35580
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_2015"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 73920
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_2045"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 75720
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_2115"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 77520
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1134"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 42720
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1154"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 43920
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1114"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 41520
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1014"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 37920
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1034"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 39120
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1054"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 40320
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1313"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 48720
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1333"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 49920
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1353"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 51120
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1254"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 47580
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1215"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 45180
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1234"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 46380
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1526"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 57000
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1546"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 58200
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1507"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 55800
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1413"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 52320
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1431"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 53460
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1448"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 54660
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1710"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 63000
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1727"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 63960
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1749"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 65280
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1649"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 61800
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1606"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 59400
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1621"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 60300
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1634"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 60960
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1945"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 72180
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1915"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 70380
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1809"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 66480
            },
            {
              "trip": {
                "gtfsId": "HSL:4731_20161024_Ti_1_1837"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 68100
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:9788KV:0:01",
            "name": "788KV",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:9788KV",
              "longName": "Rautatientori - Kuninkaanmäki - Nikkilä - Hinthaara - Porvoo",
              "shortName": "788KV"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:9788KV_20161022_Ti_1_0800"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 29760
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:4518:0:01",
            "name": "518 to Kuninkaanmäki (HSL:4970233)",
            "directionId": 0,
            "route": {
              "gtfsId": "HSL:4518",
              "longName": "Ilmala - Pasila - Kuninkaanmäki",
              "shortName": "518"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:4518_20161017_Ti_1_1740"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 64920
            },
            {
              "trip": {
                "gtfsId": "HSL:4518_20161017_Ti_1_1710"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 63120
            },
            {
              "trip": {
                "gtfsId": "HSL:4518_20161017_Ti_1_1640"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 61500
            },
            {
              "trip": {
                "gtfsId": "HSL:4518_20161017_Ti_1_1610"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 59880
            },
            {
              "trip": {
                "gtfsId": "HSL:4518_20161017_Ti_1_1540"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 58020
            },
            {
              "trip": {
                "gtfsId": "HSL:4518_20161017_Ti_1_1510"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 56160
            }
          ]
        }
      ]
    }
  }
}
        ''')


    elif request_body == '{stop(id: "HSL:1240133") {  name  code  vehicleType  stoptimesForServiceDate(date: "%s"){     pattern {         code         name         directionId         route {             gtfsId             longName             shortName         }     }     stoptimes {         trip{             gtfsId         }         stopHeadsign         serviceDay    	    realtimeArrival      }    }  }}' % (datetime.datetime.now().strftime("%Y%m%d")):
        return re.sub(r'"serviceDay":.*,',
                      '"serviceDay": ' + str(int(time.mktime(time.strptime(datetime.datetime.now().strftime("%Y%m%d"), "%Y%m%d")))) + ",",
                      '''
{
  "data": {
    "stop": {
      "vehicleType": 3,
      "stoptimesForServiceDate": [
        {
          "pattern": {
            "name": "506 to Mustialankatu (HSL:1362221) from Naistenklinikka (HSL:1150107) express",
            "route": {
              "longName": "Viikki-Arabia-Kumpula-Pasila-Meilahti",
              "shortName": "506",
              "gtfsId": "HSL:1506"
            },
            "directionId": 1,
            "code": "HSL:1506:1:02"
          },
          "stoptimes": []
        },
        {
          "pattern": {
            "name": "506 to Mustialankatu (HSL:1362221) from Naistenklinikka (HSL:1150107) via Vanhakaupunki (HSL:1270104)",
            "route": {
              "longName": "Viikki-Arabia-Kumpula-Pasila-Meilahti",
              "shortName": "506",
              "gtfsId": "HSL:1506"
            },
            "directionId": 1,
            "code": "HSL:1506:1:01"
          },
          "stoptimes": []
        },
        {
          "pattern": {
            "name": "55 to Rautatientori (HSL:1020201)",
            "route": {
              "longName": "Rautatientori-Koskela",
              "shortName": "55",
              "gtfsId": "HSL:1055"
            },
            "directionId": 1,
            "code": "HSL:1055:1:01"
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_2322"
              },
              "realtimeArrival": 84480,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_2252"
              },
              "realtimeArrival": 82680,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_2222"
              },
              "realtimeArrival": 80880,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_2352"
              },
              "realtimeArrival": 86280,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_2032"
              },
              "realtimeArrival": 74340,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_2012"
              },
              "realtimeArrival": 73140,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_2052"
              },
              "realtimeArrival": 75540,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_2152"
              },
              "realtimeArrival": 79140,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_2132"
              },
              "realtimeArrival": 77940,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_2112"
              },
              "realtimeArrival": 76740,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1112"
              },
              "realtimeArrival": 40800,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1042"
              },
              "realtimeArrival": 39000,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1057"
              },
              "realtimeArrival": 39900,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1027"
              },
              "realtimeArrival": 38100,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1012"
              },
              "realtimeArrival": 37200,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1457"
              },
              "realtimeArrival": 54360,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1442"
              },
              "realtimeArrival": 53460,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1412"
              },
              "realtimeArrival": 51660,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1427"
              },
              "realtimeArrival": 52560,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1357"
              },
              "realtimeArrival": 50760,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1557"
              },
              "realtimeArrival": 57900,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1542"
              },
              "realtimeArrival": 57060,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1512"
              },
              "realtimeArrival": 55260,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1527"
              },
              "realtimeArrival": 56160,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1212"
              },
              "realtimeArrival": 44400,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1227"
              },
              "realtimeArrival": 45300,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1157"
              },
              "realtimeArrival": 43500,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1142"
              },
              "realtimeArrival": 42600,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1127"
              },
              "realtimeArrival": 41700,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1342"
              },
              "realtimeArrival": 49860,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1312"
              },
              "realtimeArrival": 48060,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1327"
              },
              "realtimeArrival": 48960,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1257"
              },
              "realtimeArrival": 47160,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1242"
              },
              "realtimeArrival": 46200,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1852"
              },
              "realtimeArrival": 68400,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1832"
              },
              "realtimeArrival": 67200,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1812"
              },
              "realtimeArrival": 66000,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1952"
              },
              "realtimeArrival": 71940,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1932"
              },
              "realtimeArrival": 70740,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1912"
              },
              "realtimeArrival": 69600,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1612"
              },
              "realtimeArrival": 58800,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1627"
              },
              "realtimeArrival": 59700,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1657"
              },
              "realtimeArrival": 61500,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1642"
              },
              "realtimeArrival": 60600,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1742"
              },
              "realtimeArrival": 64200,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1712"
              },
              "realtimeArrival": 62400,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1727"
              },
              "realtimeArrival": 63300,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_1757"
              },
              "realtimeArrival": 65100,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_0520"
              },
              "realtimeArrival": 19560,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_0550"
              },
              "realtimeArrival": 21360,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_0640"
              },
              "realtimeArrival": 24360,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_0620"
              },
              "realtimeArrival": 23160,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_0942"
              },
              "realtimeArrival": 35340,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_0957"
              },
              "realtimeArrival": 36300,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_0927"
              },
              "realtimeArrival": 34440,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_0912"
              },
              "realtimeArrival": 33540,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_0740"
              },
              "realtimeArrival": 28020,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_0757"
              },
              "realtimeArrival": 29040,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_0720"
              },
              "realtimeArrival": 26760,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_0700"
              },
              "realtimeArrival": 25560,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_0842"
              },
              "realtimeArrival": 31740,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_0857"
              },
              "realtimeArrival": 32640,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_0827"
              },
              "realtimeArrival": 30840,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161114_La_2_0812"
              },
              "realtimeArrival": 29940,
              "stopHeadsign": "Rautatientori via Kalasatama(M)",
              "serviceDay": 1480111200
            }
          ]
        }
      ],
      "name": "A.I. Virtasen aukio",
      "code": "3597"
    }
  }
}
        ''')

    elif request_body == '{stop(id: "HSL:6070226") {  name  code  vehicleType  stoptimesForServiceDate(date: "%s"){     pattern {         code         name         directionId         route {             gtfsId             longName             shortName         }     }     stoptimes {         trip{             gtfsId         }         stopHeadsign         serviceDay    	    realtimeArrival      }    }  }}' % (
        datetime.datetime.now().strftime("%Y%m%d")):
        return re.sub(r'"serviceDay":.*,',
                      '"serviceDay": ' + str(
                          int(time.mktime(time.strptime(datetime.datetime.now().strftime("%Y%m%d"), "%Y%m%d")))) + ",",
                      '''
{
  "data": {
    "stop": {
      "vehicleType": 3,
      "stoptimesForServiceDate": [
        {
          "pattern": {
            "name": "173 to Kamppi, tulo (HSL:1040289)",
            "route": {
              "longName": "Kamppi-Masala-Kirkkonummi-Upinniemi",
              "shortName": "173",
              "gtfsId": "HSL:6173"
            },
            "directionId": 1,
            "code": "HSL:6173:1:01"
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:6173_20161114_La_2_0755"
              },
              "realtimeArrival": 29940,
              "stopHeadsign": "Kamppi",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161114_La_2_0655"
              },
              "realtimeArrival": 26340,
              "stopHeadsign": "Kamppi",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161114_La_2_0555"
              },
              "realtimeArrival": 22740,
              "stopHeadsign": "Kamppi",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161114_La_2_0900"
              },
              "realtimeArrival": 33840,
              "stopHeadsign": "Kamppi",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161114_La_2_2155"
              },
              "realtimeArrival": 80340,
              "stopHeadsign": "Kamppi",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161114_La_2_2255"
              },
              "realtimeArrival": 83940,
              "stopHeadsign": "Kamppi",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161114_La_2_2100"
              },
              "realtimeArrival": 77040,
              "stopHeadsign": "Kamppi",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161114_La_2_2000"
              },
              "realtimeArrival": 73440,
              "stopHeadsign": "Kamppi",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161114_La_2_2455"
              },
              "realtimeArrival": 91140,
              "stopHeadsign": "Kamppi",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161114_La_2_2355"
              },
              "realtimeArrival": 87540,
              "stopHeadsign": "Kamppi",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161114_La_2_1700"
              },
              "realtimeArrival": 62640,
              "stopHeadsign": "Kamppi",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161114_La_2_1600"
              },
              "realtimeArrival": 59040,
              "stopHeadsign": "Kamppi",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161114_La_2_1500"
              },
              "realtimeArrival": 55440,
              "stopHeadsign": "Kamppi",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161114_La_2_1400"
              },
              "realtimeArrival": 51840,
              "stopHeadsign": "Kamppi",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161114_La_2_1900"
              },
              "realtimeArrival": 69840,
              "stopHeadsign": "Kamppi",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161114_La_2_1800"
              },
              "realtimeArrival": 66240,
              "stopHeadsign": "Kamppi",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161114_La_2_1300"
              },
              "realtimeArrival": 48240,
              "stopHeadsign": "Kamppi",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161114_La_2_1200"
              },
              "realtimeArrival": 44640,
              "stopHeadsign": "Kamppi",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161114_La_2_1100"
              },
              "realtimeArrival": 41040,
              "stopHeadsign": "Kamppi",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161114_La_2_1000"
              },
              "realtimeArrival": 37440,
              "stopHeadsign": "Kamppi",
              "serviceDay": 1480111200
            }
          ]
        },
        {
          "pattern": {
            "name": "903K to Kirkkonummi mk (HSL:6040288)",
            "route": {
              "longName": "Kirkkonummi-Kantvik-Hila",
              "shortName": "903K",
              "gtfsId": "HSL:6903K"
            },
            "directionId": 1,
            "code": "HSL:6903K:1:01"
          },
          "stoptimes": []
        },
        {
          "pattern": {
            "name": "172 to Kamppi, tulo (HSL:1040289)",
            "route": {
              "longName": "Kamppi-Masala-Kirkkonummi-Kantvik",
              "shortName": "172",
              "gtfsId": "HSL:6172"
            },
            "directionId": 1,
            "code": "HSL:6172:1:01"
          },
          "stoptimes": []
        },
        {
          "pattern": {
            "name": "173Z to Kamppi, tulo (HSL:1040289)",
            "route": {
              "longName": "Kamppi-Kirkkonummi-Upinniemi",
              "shortName": "173Z",
              "gtfsId": "HSL:6173Z"
            },
            "directionId": 1,
            "code": "HSL:6173Z:1:01"
          },
          "stoptimes": []
        }
      ],
      "name": "Aamuruskonkuja",
      "code": "Ki0726"
    }
  }
}
        ''')

    elif request_body == '{stop(id: "HSL:1171403") {  name  code  vehicleType  stoptimesForServiceDate(date: "%s"){     pattern {         code         name         directionId         route {             gtfsId             longName             shortName         }     }     stoptimes {         trip{             gtfsId         }         stopHeadsign         serviceDay    	    realtimeArrival      }    }  }}' % (
    datetime.datetime.now().strftime("%Y%m%d")):
        return re.sub(r'"serviceDay":.*,',
                      '"serviceDay": ' + str(
                          int(time.mktime(time.strptime(datetime.datetime.now().strftime("%Y%m%d"), "%Y%m%d")))) + ",",
                      '''
{
  "data": {
    "stop": {
      "vehicleType": 0,
      "stoptimesForServiceDate": [
        {
          "pattern": {
            "name": "7B to Töölön halli (HSL:1140439)",
            "route": {
              "longName": "Senaatintori-Pasila-Töölö-Senaatintori",
              "shortName": "7B",
              "gtfsId": "HSL:1007B"
            },
            "directionId": 1,
            "code": "HSL:1007B:1:04"
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:1007B5_20161114_La_2_2316"
              },
              "realtimeArrival": 84120,
              "stopHeadsign": "Töölö",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B5_20161114_La_2_2328"
              },
              "realtimeArrival": -1,
              "stopHeadsign": "Töölö",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B5_20161114_La_2_2340"
              },
              "realtimeArrival": 85560,
              "stopHeadsign": "Töölö",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B5_20161114_La_2_2305"
              },
              "realtimeArrival": 83460,
              "stopHeadsign": "Töölö",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B5_20161114_La_2_1915"
              },
              "realtimeArrival": 69660,
              "stopHeadsign": "Töölö",
              "serviceDay": 1480111200
            }
          ]
        },
        {
          "pattern": {
            "name": "7B to Hallituskatu (HSL:1010420) from Pasilan asema (HSL:1174401)",
            "route": {
              "longName": "Senaatintori-Pasila-Töölö-Senaatintori",
              "shortName": "7B",
              "gtfsId": "HSL:1007B"
            },
            "directionId": 1,
            "code": "HSL:1007B:1:02"
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_2132"
              },
              "realtimeArrival": 77880,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_2143"
              },
              "realtimeArrival": 78540,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_2107"
              },
              "realtimeArrival": 76380,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_2120"
              },
              "realtimeArrival": 77160,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_2156"
              },
              "realtimeArrival": 79320,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_2208"
              },
              "realtimeArrival": 80040,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_2219"
              },
              "realtimeArrival": 80700,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_2254"
              },
              "realtimeArrival": 82800,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_2230"
              },
              "realtimeArrival": 81360,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_2242"
              },
              "realtimeArrival": 82080,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_2003"
              },
              "realtimeArrival": 72540,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_2017"
              },
              "realtimeArrival": 73380,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_2054"
              },
              "realtimeArrival": 75600,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_2030"
              },
              "realtimeArrival": 74160,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_2043"
              },
              "realtimeArrival": 74940,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_0830"
              },
              "realtimeArrival": 30960,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_0803"
              },
              "realtimeArrival": 29340,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_0817"
              },
              "realtimeArrival": 30180,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_0841"
              },
              "realtimeArrival": 31620,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_0852"
              },
              "realtimeArrival": 32280,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_0902"
              },
              "realtimeArrival": 32880,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_0912"
              },
              "realtimeArrival": 33480,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_0942"
              },
              "realtimeArrival": 35280,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_0952"
              },
              "realtimeArrival": 35880,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_0922"
              },
              "realtimeArrival": 34080,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_0932"
              },
              "realtimeArrival": 34680,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_0556"
              },
              "realtimeArrival": 21660,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_0625"
              },
              "realtimeArrival": 23400,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_0611"
              },
              "realtimeArrival": 22560,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_0641"
              },
              "realtimeArrival": 24360,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_0656"
              },
              "realtimeArrival": 25260,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_0713"
              },
              "realtimeArrival": 26340,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_0742"
              },
              "realtimeArrival": 28080,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_0727"
              },
              "realtimeArrival": 27180,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1911"
              },
              "realtimeArrival": 69420,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1926"
              },
              "realtimeArrival": 70320,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1900"
              },
              "realtimeArrival": 68760,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1952"
              },
              "realtimeArrival": 71880,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1939"
              },
              "realtimeArrival": 71100,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1639"
              },
              "realtimeArrival": 60300,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1618"
              },
              "realtimeArrival": 59040,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1628"
              },
              "realtimeArrival": 59640,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1650"
              },
              "realtimeArrival": 60960,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1710"
              },
              "realtimeArrival": 62160,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1720"
              },
              "realtimeArrival": 62760,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1700"
              },
              "realtimeArrival": 61560,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1752"
              },
              "realtimeArrival": 64680,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1731"
              },
              "realtimeArrival": 63420,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1742"
              },
              "realtimeArrival": 64080,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1802"
              },
              "realtimeArrival": 65280,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1834"
              },
              "realtimeArrival": 67200,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1847"
              },
              "realtimeArrival": 67980,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1812"
              },
              "realtimeArrival": 65880,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1823"
              },
              "realtimeArrival": 66540,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1403"
              },
              "realtimeArrival": 50940,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1434"
              },
              "realtimeArrival": 52800,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1444"
              },
              "realtimeArrival": 53400,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1414"
              },
              "realtimeArrival": 51600,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1424"
              },
              "realtimeArrival": 52200,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1455"
              },
              "realtimeArrival": 54060,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1516"
              },
              "realtimeArrival": 55320,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1526"
              },
              "realtimeArrival": 55920,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1506"
              },
              "realtimeArrival": 54720,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1558"
              },
              "realtimeArrival": 57840,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1536"
              },
              "realtimeArrival": 56520,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1547"
              },
              "realtimeArrival": 57180,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1608"
              },
              "realtimeArrival": 58440,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1208"
              },
              "realtimeArrival": 44040,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1240"
              },
              "realtimeArrival": 45960,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1250"
              },
              "realtimeArrival": 46560,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1219"
              },
              "realtimeArrival": 44700,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1230"
              },
              "realtimeArrival": 45360,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1311"
              },
              "realtimeArrival": 47820,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1322"
              },
              "realtimeArrival": 48480,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1300"
              },
              "realtimeArrival": 47160,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1352"
              },
              "realtimeArrival": 50280,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1332"
              },
              "realtimeArrival": 49080,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1342"
              },
              "realtimeArrival": 49680,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1002"
              },
              "realtimeArrival": 36480,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1033"
              },
              "realtimeArrival": 38340,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1044"
              },
              "realtimeArrival": 39000,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1012"
              },
              "realtimeArrival": 37080,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1022"
              },
              "realtimeArrival": 37680,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1055"
              },
              "realtimeArrival": 39660,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1116"
              },
              "realtimeArrival": 40920,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1127"
              },
              "realtimeArrival": 41580,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1106"
              },
              "realtimeArrival": 40320,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1158"
              },
              "realtimeArrival": 43440,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1138"
              },
              "realtimeArrival": 42240,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_La_2_1148"
              },
              "realtimeArrival": 42840,
              "stopHeadsign": "Senaatintori via Ooppera",
              "serviceDay": 1480111200
            }
          ]
        },
        {
          "pattern": {
            "name": "7B to Rautatieasema (HSL:1020453)",
            "route": {
              "longName": "Senaatintori-Pasila-Töölö-Senaatintori",
              "shortName": "7B",
              "gtfsId": "HSL:1007B"
            },
            "directionId": 1,
            "code": "HSL:1007B:1:03"
          },
          "stoptimes": []
        }
      ],
      "name": "Palkkatilanportti",
      "code": "0604"
    }
  }
}
        ''')
    
    elif request_body == '{trip(id: "HSL:1506_20161031_Ti_2_1155") { stoptimesForDate(serviceDay: "%s") {      stop{          gtfsId          name          code }      serviceDay      realtimeArrival        }       }      }}' % (datetime.datetime.now().strftime("%Y%m%d")):
        return re.sub(r'"serviceDay":.*,',
                      '"serviceDay": ' + str(int(time.mktime(time.strptime(datetime.datetime.now().strftime("%Y%m%d"), "%Y%m%d")))) + ",",
                      '''
{
  "data": {
    "trip": {
      "stoptimesForDate": [
        {
          "stop": {
            "gtfsId": "HSL:1150107",
            "name": "Naistenklinikka",
            "code": "1321"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 42900
        },
        {
          "stop": {
            "gtfsId": "HSL:1150118",
            "name": "Tukholmankatu",
            "code": "1380"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 42960
        },
        {
          "stop": {
            "gtfsId": "HSL:1150134",
            "name": "Töölön tulli",
            "code": "1378"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 43020
        },
        {
          "stop": {
            "gtfsId": "HSL:1180124",
            "name": "Reijolankatu",
            "code": "2076"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 43140
        },
        {
          "stop": {
            "gtfsId": "HSL:1171122",
            "name": "Auroran sairaala",
            "code": "2073"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 43200
        },
        {
          "stop": {
            "gtfsId": "HSL:1171134",
            "name": "Eläintarha",
            "code": "2109"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 43260
        },
        {
          "stop": {
            "gtfsId": "HSL:1171152",
            "name": "Palkkatilanportti",
            "code": "2107"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 43380
        },
        {
          "stop": {
            "gtfsId": "HSL:1173105",
            "name": "Pasilan asema",
            "code": "2181"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 43500
        },
        {
          "stop": {
            "gtfsId": "HSL:1173107",
            "name": "Vaihdemiehenkatu",
            "code": "2183"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 43560
        },
        {
          "stop": {
            "gtfsId": "HSL:1173132",
            "name": "Ilmattarentie",
            "code": "2193"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 43680
        },
        {
          "stop": {
            "gtfsId": "HSL:1250111",
            "name": "Kalervonkatu",
            "code": "3059"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 43740
        },
        {
          "stop": {
            "gtfsId": "HSL:1250113",
            "name": "Olympiakylä",
            "code": "3061"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 43800
        },
        {
          "stop": {
            "gtfsId": "HSL:1250115",
            "name": "Joukolan puisto",
            "code": "3063"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 43860
        },
        {
          "stop": {
            "gtfsId": "HSL:1250106",
            "name": "Joukolan puisto",
            "code": "3082"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 43920
        },
        {
          "stop": {
            "gtfsId": "HSL:1240108",
            "name": "Kumpula",
            "code": "3080"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 44040
        },
        {
          "stop": {
            "gtfsId": "HSL:1240131",
            "name": "Intiankatu",
            "code": "3599"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 44040
        },
        {
          "stop": {
            "gtfsId": "HSL:1240133",
            "name": "A.I. Virtasen aukio",
            "code": "3597"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 44160
        },
        {
          "stop": {
            "gtfsId": "HSL:1230109",
            "name": "Kumpulan kampus",
            "code": "3037"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 44280
        },
        {
          "stop": {
            "gtfsId": "HSL:1230113",
            "name": "Kokkosaarenkatu",
            "code": "3041"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 44340
        },
        {
          "stop": {
            "gtfsId": "HSL:1230104",
            "name": "Arabia",
            "code": "3043"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 44400
        },
        {
          "stop": {
            "gtfsId": "HSL:1230102",
            "name": "Kaironkatu",
            "code": "3045"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 44460
        },
        {
          "stop": {
            "gtfsId": "HSL:1270103",
            "name": "Annalantie",
            "code": "3047"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 44520
        },
        {
          "stop": {
            "gtfsId": "HSL:1361103",
            "name": "Viikinranta",
            "code": "3071"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 44640
        },
        {
          "stop": {
            "gtfsId": "HSL:1361105",
            "name": "Hernepellonkuja",
            "code": "3073"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 44700
        },
        {
          "stop": {
            "gtfsId": "HSL:1361107",
            "name": "Maaherrantie",
            "code": "3075"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 44760
        },
        {
          "stop": {
            "gtfsId": "HSL:1362107",
            "name": "Viikin tiedepuisto",
            "code": "3240"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 44820
        },
        {
          "stop": {
            "gtfsId": "HSL:1362125",
            "name": "Viikki",
            "code": "3463"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 44880
        },
        {
          "stop": {
            "gtfsId": "HSL:1362132",
            "name": "Ylioppilaskylä",
            "code": "3465"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 44940
        },
        {
          "stop": {
            "gtfsId": "HSL:1362221",
            "name": "Mustialankatu",
            "code": "3477"
          },
          "serviceDay": 1478556000,
          "realtimeArrival": 45000
        }
      ]
    }
  }
}
        ''')

    elif request_body == '{ trip(id:\"trip_id_1\"){\n                        gtfsId\n                        stoptimesForDate(serviceDay:"%s"){\n                            serviceDay\n                            realtimeArrival\n                            stop{\n                                gtfsId\n                            }\n                            }\n                        }\n                    }'  % (datetime.datetime.now().strftime("%Y%m%d")):
        return re.sub(r'"serviceDay":.*,',
               '"serviceDay": ' + str(int(time.mktime(time.strptime(datetime.datetime.now().strftime("%Y%m%d"), "%Y%m%d")))) + ",",
               '''
{
    "data": {
        "trip": {
            "gtfsId": "trip_id_1",
            "stoptimesForDate": [
                {
                    "serviceDay": 1479765600,
                    "realtimeArrival": 0,
                    "stop": {
                        "gtfsId": "stop_id"
                    }
                }
            ]
        }
    }
}
        ''')

    elif request_body == '{ trip(id:\"trip_id_2\"){\n                        gtfsId\n                        stoptimesForDate(serviceDay:"%s"){\n                            serviceDay\n                            realtimeArrival\n                            stop{\n                                gtfsId\n                            }\n                            }\n                        }\n                    }' % (datetime.datetime.now().strftime("%Y%m%d")):
        return re.sub(r'"serviceDay":.*,',
               '"serviceDay": ' + str(
                   int(time.mktime(time.strptime(datetime.datetime.now().strftime("%Y%m%d"), "%Y%m%d")))) + ",",
               '''
{
    "data": {
        "trip": {
            "gtfsId": "trip_id_2",
            "stoptimesForDate": [
                {
                    "serviceDay": 1479765600,
                    "realtimeArrival": 0,
                    "stop": {
                        "gtfsId": "stop_id"
                    }
                }
            ]
        }
    }
}
        ''')

    elif request_body == '{ trip(id:"trip_id_3"){\n                        gtfsId\n                        stoptimesForDate(serviceDay:"%s"){\n                            serviceDay\n                            realtimeArrival\n                            stop{\n                                gtfsId\n                            }\n                            }\n                        }\n                    }' % (datetime.datetime.now().strftime("%Y%m%d")):
        return re.sub(r'"serviceDay":.*,',
               '"serviceDay": ' + str(
                   int(time.mktime(time.strptime(datetime.datetime.now().strftime("%Y%m%d"), "%Y%m%d")))) + ",",
               '''
{
    "data": {
        "trip": {
            "gtfsId": "trip_id_3",
            "stoptimesForDate": [
                {
                    "serviceDay": 1479765600,
                    "realtimeArrival": 99999,
                    "stop": {
                        "gtfsId": "stop_id"
                    }
                }
            ]
        }
    }
}
        ''')

    else:
        return 'your mock call didn\'t match any request body'


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=11111)
