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
        },
        {
          "node": {
            "distance": 176,
            "stop": {
              "gtfsId": "MATKA:165925",
              "name": "Kumpulan kampus",
              "vehicleType": -999
            }
          }
        },
        {
          "node": {
            "distance": 196,
            "stop": {
              "gtfsId": "HSL:1240118",
              "name": "Kumpulan kampus",
              "vehicleType": 3
            }
          }
        },
        {
          "node": {
            "distance": 253,
            "stop": {
              "gtfsId": "MATKA:165922",
              "name": "Kumpulan kampus",
              "vehicleType": -999
            }
          }
        },
        {
          "node": {
            "distance": 263,
            "stop": {
              "gtfsId": "HSL:1240103",
              "name": "Kumpulan kampus",
              "vehicleType": 3
            }
          }
        }
      ]
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
              "serviceDay": 1478556000,
              "realtimeArrival": 56820
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1509"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 55860
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1554"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 58620
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1539"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 57720
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1639"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 61260
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1624"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 60420
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1609"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 59520
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1654"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 62160
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1454"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 54960
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1906"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 69900
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1946"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 72300
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1926"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 71100
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1746"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 65160
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1726"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 63960
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1709"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 63000
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1846"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 68760
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1826"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 67560
            },
            {
              "trip": {
                "gtfsId": "HSL:4718_20161017_Ti_1_1806"
              },
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
              "serviceDay": 1478556000,
              "realtimeArrival": 20100
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_0550"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 21900
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_0620"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 23880
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_0649"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 25620
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_0738"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 28620
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_0715"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 27240
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_0850"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 32940
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_0800"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 29940
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_0820"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 31140
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1000"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 37140
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1100"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 40740
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1200"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 44340
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1300"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 48000
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1350"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 51000
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1442"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 54180
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1502"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 55440
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1520"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 56520
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1542"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 57900
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1600"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 58980
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1620"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 60180
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1635"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 61020
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1655"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 62160
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1725"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 63840
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1800"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 65940
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_1900"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 69480
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_2100"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 76680
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_2000"
              },
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
              "serviceDay": 1478556000,
              "realtimeArrival": 51540
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1430"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 53400
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1530"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 57180
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1500"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 55200
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1630"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 60720
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1600"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 58980
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1755"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 65640
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1700"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 62400
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1055"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 40380
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1155"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 44040
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1300"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 47940
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1330"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 49740
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1855"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 69180
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_1955"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 72780
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_0955"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 36780
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_0600"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 22500
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_0630"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 24420
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_0730"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 28140
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_0700"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 26280
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_0800"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 29940
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_0855"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 33180
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_2310"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 84360
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_2155"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 79860
            },
            {
              "trip": {
                "gtfsId": "HSL:4717A_20161017_Ti_1_2055"
              },
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
              "serviceDay": 1478556000,
              "realtimeArrival": 79260
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_2042"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 75600
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_2351"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 86760
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_2251"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 83220
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1042"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 39660
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1242"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 46860
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1142"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 43260
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1400"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 51540
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1428"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 53280
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1330"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 49740
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1600"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 58980
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1630"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 60780
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1500"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 55320
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1530"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 57180
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1844"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 68520
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1700"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 62520
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1730"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 64200
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1800"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 65880
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_1942"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 72000
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_0535"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 20940
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_0730"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 28200
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_0800"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 30000
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_0630"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 24420
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_0700"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 26340
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_0842"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 32460
            },
            {
              "trip": {
                "gtfsId": "HSL:4739_20161024_Ti_1_0942"
              },
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
              "serviceDay": 1478556000,
              "realtimeArrival": 67620
            },
            {
              "trip": {
                "gtfsId": "HSL:9787A_20161022_Ti_1_1615"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 59640
            },
            {
              "trip": {
                "gtfsId": "HSL:9787A_20161022_Ti_1_2000"
              },
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
              "serviceDay": 1478556000,
              "realtimeArrival": 70380
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1935"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 71580
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1515"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 56220
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1445"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 54300
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1415"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 52500
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1615"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 59880
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1545"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 58080
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1715"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 63300
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1735"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 64440
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1645"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 61500
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1835"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 67980
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1815"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 66780
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1015"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 37980
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1035"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 39180
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1135"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 42780
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1115"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 41580
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1215"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 45240
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1235"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 46440
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1345"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 50640
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_1315"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 48840
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_2015"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 73980
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_2035"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 75180
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_2135"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 78660
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_2115"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 77580
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_2215"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 81060
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_2240"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 82560
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_0645"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 25320
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_0615"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 23400
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_0715"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 27240
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_0745"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 29040
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_0835"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 31980
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_0815"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 30840
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_0915"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 34380
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_0935"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 35580
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_0520"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 19980
            },
            {
              "trip": {
                "gtfsId": "HSL:4717_20161017_Ti_1_0540"
              },
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
              "serviceDay": 1478556000,
              "realtimeArrival": 38580
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1125"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 42240
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1225"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 45840
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1325"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 49440
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1425"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 53040
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1925"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 70980
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1450"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 54720
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1510"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 55920
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1550"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 58440
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1528"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 57120
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1610"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 59640
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1640"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 61320
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1740"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 64740
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1710"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 63000
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1848"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 68760
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_1820"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 67080
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_2315"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 84660
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_2025"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 74580
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_2125"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 78120
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_2215"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 81120
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_0635"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 24720
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_0605"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 22800
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_0735"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 28440
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_0705"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 26580
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_0805"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 30300
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_0835"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 32040
            },
            {
              "trip": {
                "gtfsId": "HSL:4724_20161024_Ti_1_0926"
              },
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
              "serviceDay": 1478556000,
              "realtimeArrival": 59820
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1604"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 59280
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1634"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 60960
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1624"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 60360
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1654"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 62160
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1644"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 61560
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1716"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 63420
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1704"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 62700
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1738"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 64680
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1727"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 64020
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1758"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 65820
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1748"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 65280
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1809"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 66480
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1825"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 67440
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1845"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 68640
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1925"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 71040
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1945"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 72180
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1905"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 69840
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_2006"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 73440
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_2026"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 74580
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_2046"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 75780
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_2207"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 80580
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_2106"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 76980
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_2126"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 78180
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_2146"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 79320
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_2323"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 85080
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_2227"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 81780
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_2253"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 83280
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0721"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 27600
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0711"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 26940
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0741"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 28860
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0731"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 28260
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0751"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 29460
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0844"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 32580
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0831"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 31860
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0801"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 30060
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0821"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 31260
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0811"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 30660
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0904"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 33780
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0924"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 34980
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0944"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 36180
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0553"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 22020
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0613"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 23340
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0633"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 24600
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_0653"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 25860
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1204"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 44580
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1224"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 45780
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1124"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 42372
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1144"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 43380
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1304"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 48240
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1339"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 50340
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1324"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 49440
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1354"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 51240
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1244"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 46980
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1409"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 52140
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1439"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 54000
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1424"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 53040
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1454"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 54960
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1514"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 56160
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1504"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 55560
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1534"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 57480
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1524"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 56820
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1554"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 58680
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1544"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 58080
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1104"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 40980
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1004"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 37380
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1024"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 38580
            },
            {
              "trip": {
                "gtfsId": "HSL:1077_20161017_Ti_1_1044"
              },
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
      "name": "A.I. Virtasen aukio",
      "code": "3597",
      "vehicleType": 3,
      "stoptimesForServiceDate": [
        {
          "pattern": {
            "code": "HSL:1055:1:01",
            "name": "55 to Rautatientori (HSL:1020201)",
            "directionId": 1,
            "route": {
              "gtfsId": "HSL:1055",
              "longName": "Rautatientori - Koskela",
              "shortName": "55"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1832"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 67200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1812"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 66000
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1852"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 68400
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1952"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 71940
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1932"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 70740
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1912"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 69540
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1641"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 60540
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1626"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 59640
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1611"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 58800
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1556"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 57900
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1541"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 57000
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1726"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 63240
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1711"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 62340
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1757"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 65100
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1742"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 64200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1656"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 61440
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1329"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 49020
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1314"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 48120
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1359"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 50820
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1344"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 49920
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1526"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 56100
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1511"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 55200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1443"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 53520
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1429"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 52680
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1414"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 51780
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1457"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 54360
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1158"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 43560
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1143"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 42676
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1128"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": -1
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1113"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 40860
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1258"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 47160
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1243"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 46260
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1228"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 45360
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1213"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 44460
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1043"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 39060
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1028"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 38160
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1013"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 37260
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1058"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 39960
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_2256"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 82920
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_2226"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 81120
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_2356"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 86520
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_2326"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 84720
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_2012"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 73140
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_2052"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 75540
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_2032"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 74340
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_2132"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 77940
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_2112"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 76740
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_2154"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 79260
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0914"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 33780
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0958"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 36360
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0943"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 35460
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0928"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 34560
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0759"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 29280
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0746"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 28500
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0736"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 27900
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0725"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 27240
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0713"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 26520
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0859"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 32880
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0844"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 31980
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0829"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 31080
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0814"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 30180
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0550"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 21420
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0520"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 19620
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0628"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 23700
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0610"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 22620
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0659"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 25620
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0644"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 24720
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:1506:1:02",
            "name": "506 to Mustialankatu (HSL:1362221) from Naistenklinikka (HSL:1150107) express",
            "directionId": 1,
            "route": {
              "gtfsId": "HSL:1506",
              "longName": "Viikki - Arabia - Kumpula - Pasila - Meilahti",
              "shortName": "506"
            }
          },
          "stoptimes": []
        },
        {
          "pattern": {
            "code": "HSL:1506:1:01",
            "name": "506 to Mustialankatu (HSL:1362221) from Naistenklinikka (HSL:1150107) via Vanhakaupunki (HSL:1270104)",
            "directionId": 1,
            "route": {
              "gtfsId": "HSL:1506",
              "longName": "Viikki - Arabia - Kumpula - Pasila - Meilahti",
              "shortName": "506"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_2308"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 84240
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_2208"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 80700
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_2238"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 82500
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_2115"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 77640
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_2138"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 78960
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_2045"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 75900
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_2015"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 74100
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1235"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 46560
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1255"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 47760
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1215"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 45360
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1115"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 41760
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1135"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 42960
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1155"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 44160
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1015"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 38100
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1035"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 39300
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1055"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 40560
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1639"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 61500
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1655"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 62400
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1608"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 59820
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1623"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 60600
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1555"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 59040
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1519"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 56820
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1531"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 57600
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1543"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 58320
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1507"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 56040
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1435"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 54000
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1453"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 55140
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1415"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 52740
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1355"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 51480
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1315"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 49020
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1335"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 50220
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1845"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 68760
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1915"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 70560
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1945"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 72300
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1755"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 65820
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1715"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 63540
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1735"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 64740
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_1815"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 67020
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_0743"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 29220
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_0757"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 30060
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_0827"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 31920
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_0842"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 32820
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_0857"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 33600
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_0812"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 30960
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_0620"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 23940
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_0640"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 25200
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_0659"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 26400
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_0714"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 27360
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_0729"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 28320
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_0540"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 21240
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_0520"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 20040
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_0600"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 22560
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_0942"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 36180
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_0957"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 37020
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_0912"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 34440
            },
            {
              "trip": {
                "gtfsId": "HSL:1506_20161104_Ti_2_0927"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 35280
            }
          ]
        }
      ]
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
      "name": "Aamuruskonkuja",
      "code": "Ki0726",
      "vehicleType": 3,
      "stoptimesForServiceDate": [
        {
          "pattern": {
            "code": "HSL:6173:1:01",
            "name": "173 to Kamppi, tulo (HSL:1040289)",
            "directionId": 1,
            "route": {
              "gtfsId": "HSL:6173",
              "longName": "Kamppi - Masala - Kirkkonummi - Upinniemi",
              "shortName": "173"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_1800"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 66060
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_1900"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 69600
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_1300"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 48060
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_1400"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 51660
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_1100"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 40860
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_1200"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 44460
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_1000"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 37260
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_2255"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 83700
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_2355"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 87300
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_2000"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 73200
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_2155"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 80100
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_2100"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 76800
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_0455"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 18900
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_0600"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 22860
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:6903K:1:01",
            "name": "903K to Kirkkonummi mk (HSL:6040288)",
            "directionId": 1,
            "route": {
              "gtfsId": "HSL:6903K",
              "longName": "Kirkkonummi - Kantvik - Hila",
              "shortName": "903K"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:6903K_20161107_Ma_2_0915"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 34560
            },
            {
              "trip": {
                "gtfsId": "HSL:6903K_20161107_Ma_2_0811"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 30900
            },
            {
              "trip": {
                "gtfsId": "HSL:6903K_20161107_Ma_2_0710"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 27180
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:6172:1:01",
            "name": "172 to Kamppi, tulo (HSL:1040289)",
            "directionId": 1,
            "route": {
              "gtfsId": "HSL:6172",
              "longName": "Kamppi - Masala - Kirkkonummi - Kantvik",
              "shortName": "172"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:6172_20161107_Ma_2_1540"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 56640
            },
            {
              "trip": {
                "gtfsId": "HSL:6172_20161107_Ma_2_1625"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 59340
            },
            {
              "trip": {
                "gtfsId": "HSL:6172_20161107_Ma_2_1655"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 61140
            },
            {
              "trip": {
                "gtfsId": "HSL:6172_20161107_Ma_2_1725"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 62940
            },
            {
              "trip": {
                "gtfsId": "HSL:6172_20161107_Ma_2_1755"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 64740
            },
            {
              "trip": {
                "gtfsId": "HSL:6172_20161107_Ma_2_0640"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 24240
            },
            {
              "trip": {
                "gtfsId": "HSL:6172_20161107_Ma_2_0740"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 27840
            },
            {
              "trip": {
                "gtfsId": "HSL:6172_20161107_Ma_2_0710"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 26040
            },
            {
              "trip": {
                "gtfsId": "HSL:6172_20161107_Ma_2_0810"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 29640
            },
            {
              "trip": {
                "gtfsId": "HSL:6172_20161107_Ma_2_0840"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 31440
            },
            {
              "trip": {
                "gtfsId": "HSL:6172_20161107_Ma_2_0910"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 33240
            },
            {
              "trip": {
                "gtfsId": "HSL:6172_20161107_Ma_2_0930"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 34440
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:6173Z:1:01",
            "name": "173Z to Kamppi, tulo (HSL:1040289)",
            "directionId": 1,
            "route": {
              "gtfsId": "HSL:6173Z",
              "longName": "Kamppi - Kirkkonummi - Upinniemi",
              "shortName": "173Z"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:6173Z_20161107_Ma_2_0635"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 25020
            },
            {
              "trip": {
                "gtfsId": "HSL:6173Z_20161107_Ma_2_0535"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 21360
            },
            {
              "trip": {
                "gtfsId": "HSL:6173Z_20161107_Ma_2_0930"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 35460
            },
            {
              "trip": {
                "gtfsId": "HSL:6173Z_20161107_Ma_2_0900"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 33660
            },
            {
              "trip": {
                "gtfsId": "HSL:6173Z_20161107_Ma_2_0830"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 31860
            },
            {
              "trip": {
                "gtfsId": "HSL:6173Z_20161107_Ma_2_0730"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 28320
            },
            {
              "trip": {
                "gtfsId": "HSL:6173Z_20161107_Ma_2_0705"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 26820
            },
            {
              "trip": {
                "gtfsId": "HSL:6173Z_20161107_Ma_2_0755"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 29820
            },
            {
              "trip": {
                "gtfsId": "HSL:6173Z_20161107_Ma_2_1530"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 57060
            },
            {
              "trip": {
                "gtfsId": "HSL:6173Z_20161107_Ma_2_1455"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 54960
            },
            {
              "trip": {
                "gtfsId": "HSL:6173Z_20161107_Ma_2_1715"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 63420
            },
            {
              "trip": {
                "gtfsId": "HSL:6173Z_20161107_Ma_2_1625"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 60360
            },
            {
              "trip": {
                "gtfsId": "HSL:6173Z_20161107_Ma_2_1600"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 58860
            },
            {
              "trip": {
                "gtfsId": "HSL:6173Z_20161107_Ma_2_1655"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 62220
            }
          ]
        }
      ]
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
      "name": "Palkkatilanportti",
      "code": "0604",
      "vehicleType": 0,
      "stoptimesForServiceDate": [
        {
          "pattern": {
            "code": "HSL:1007B:1:04",
            "name": "7B to Töölön halli (HSL:1140439)",
            "directionId": 1,
            "route": {
              "gtfsId": "HSL:1007B",
              "longName": "Senaatintori-Pasila-Töölö-Senaatintori",
              "shortName": "7B"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:1007B5_20161114_Ma_2_2308"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 83640
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B5_20161114_Ma_2_2323"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 84540
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B5_20161114_Ma_2_2347"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 85980
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B5_20161114_Ma_2_2335"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 85260
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B5_20161114_Ma_2_0938"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 35040
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:1007B:1:02",
            "name": "7B to Hallituskatu (HSL:1010420) from Pasilan asema (HSL:1174401)",
            "directionId": 1,
            "route": {
              "gtfsId": "HSL:1007B",
              "longName": "Senaatintori-Pasila-Töölö-Senaatintori",
              "shortName": "7B"
            }
          },
          "stoptimes": [
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_2052"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 75480
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_2040"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 74760
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_2028"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 74040
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_2016"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 73320
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_2004"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 72600
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_2300"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 83160
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_2248"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 82440
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_2235"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 81660
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_2221"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 80820
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_2206"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 79920
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_2150"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 78960
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_2139"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 78300
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_2127"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 77580
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_2115"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 76860
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_2103"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 76140
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1656"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 61320
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1645"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 60660
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1635"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 60060
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1625"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 59520
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1615"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 58920
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1606"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 58380
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1450"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 53760
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1558"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 57900
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1546"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 57180
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1536"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 56580
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1527"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 56040
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1517"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 55440
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1501"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 54420
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1507"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 54780
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1354"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 50400
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1343"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 49740
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1331"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 49020
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1439"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 53100
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1427"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 52380
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1416"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 51720
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1405"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 51060
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1258"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 47040
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1247"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 46380
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1235"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 45660
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1224"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 45000
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1213"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 44340
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1320"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 48360
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1309"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 47700
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1952"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 71880
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1940"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 71160
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1928"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 70440
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1916"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 69720
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1904"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 69000
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1852"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 68280
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1840"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 67560
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1828"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 66840
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1815"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 66060
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1804"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 65400
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1754"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 64800
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1743"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 64140
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1733"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 63540
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1724"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 63000
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1714"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 62400
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1705"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 61860
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1151"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 43020
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1139"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 42300
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1128"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 41640
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1117"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 40980
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1106"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 40320
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1202"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 43680
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1055"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 39660
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1043"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 38940
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1032"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 38280
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1021"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 37620
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_1010"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 36960
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_0914"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 33600
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_0901"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 32880
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_0959"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 36300
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_0947"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 35580
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_0936"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 34920
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_0925"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 34260
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_0840"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 31620
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_0849"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 32160
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_0820"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 30420
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_0829"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 30960
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_0811"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 29880
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_0802"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 29340
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_0752"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 28740
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_0743"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 28200
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_0732"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 27540
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_0723"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 27000
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_0715"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 26520
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_0706"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 25980
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_0657"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 25440
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_0641"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 24420
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_0648"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 24900
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_0632"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 23880
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_0620"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 23160
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_0606"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 22320
            },
            {
              "trip": {
                "gtfsId": "HSL:1007B_20161114_Ma_2_0554"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 21600
            }
          ]
        },
        {
          "pattern": {
            "code": "HSL:1007B:1:03",
            "name": "7B to Rautatieasema (HSL:1020453)",
            "directionId": 1,
            "route": {
              "gtfsId": "HSL:1007B",
              "longName": "Senaatintori-Pasila-Töölö-Senaatintori",
              "shortName": "7B"
            }
          },
          "stoptimes": []
        }
      ]
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
