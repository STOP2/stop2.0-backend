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

    if request_body == '{stopsByRadius(lat:60.293571, lon:25.044250, radius:1) {  edges {      node {          distance          stop {    	        gtfsId              name              vehicleType          }      }    }  }}':
        return '''
{
    "data": {
        "stopsByRadius": {
            "edges": [
                {
                    "node": {
                        "distance": 113,
                        "stop": {
                            "gtfsId": "HSL:4610207",
                            "name": "Tikkurilan matkakesk",
                            "vehicleType": 3
                        }
                    }
                }
            ]
        }
    }
}
'''

    elif request_body == '{stopsByRadius(lat:60.203978, lon:24.963357, radius:300) {  edges {      node {          distance          stop {    	        gtfsId              name              vehicleType          }      }    }  }}':
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
                "gtfsId": "HSL:4722_20161024_Ti_1_0550"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 700
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_0620"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 4300
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_0649"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 7900
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_0738"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 11500
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_0715"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 15100
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_0850"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 18700
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_0800"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 22300
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_0820"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 25900
            },
            {
              "trip": {
                "gtfsId": "HSL:4722_20161024_Ti_1_0520"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 29500
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
              "realtimeArrival": 900
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1812"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 1800
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1852"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 2700
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1952"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 3600
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1932"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 4500
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1912"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 5400
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1641"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 6300
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1626"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 7200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1611"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 8100
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1556"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 9000
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1541"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 9900
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1726"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 10800
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1711"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 11700
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1757"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 12600
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1742"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 13500
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1656"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 14400
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1329"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 15300
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1314"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 16200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1359"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 17100
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1344"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 18000
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1526"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 18900
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1511"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 19800
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1443"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 20700
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1429"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 21600
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1414"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 22500
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1457"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 23400
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1158"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 24300
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1143"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 25200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1128"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 26100
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1113"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 27000
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1258"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 27900
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1243"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 28800
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1228"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 29700
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1213"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 30600
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1043"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 31500
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1028"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 32400
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1013"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 33300
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_1058"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 34200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_2256"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 35100
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_2226"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 36000
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_2356"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 36900
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_2326"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 37800
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_2012"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 38700
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_2052"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 39600
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_2032"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 40500
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_2132"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 41400
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_2112"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 42300
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_2154"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 43200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0914"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 44100
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0958"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 45000
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0943"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 45900
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0928"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 46800
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0759"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 47700
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0746"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 48600
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0736"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 49500
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0725"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 50400
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0713"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 51300
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0859"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 52200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0844"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 53100
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0829"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 54000
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0814"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 54900
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0550"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 55800
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0520"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 56700
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0628"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 57600
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0610"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 58500
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0659"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 59400
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0644"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 60300
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0814"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 61200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0550"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 62100
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0520"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 63000
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0628"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 63900
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0610"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 64800
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0659"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 65700
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0644"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 66600
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0814"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 67500
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0550"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 68400
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0520"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 69300
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0628"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 70200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0610"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 71100
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0659"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 72000
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0644"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 72900
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0814"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 73800
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0550"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 74700
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0520"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 75600
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0628"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 76500
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0610"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 77400
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0659"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 78300
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0644"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 79200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0659"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 80100
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0644"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 81000
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0659"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 81900
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0644"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 82800
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0659"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 83700
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0644"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 84600
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0644"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 85500
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0659"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 86400
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0644"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 87300
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0644"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 88200
            },
            {
              "trip": {
                "gtfsId": "HSL:1055_20161017_Ti_2_0659"
              },
              "serviceDay": 1478556000,
              "realtimeArrival": 89100
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
              "realtimeArrival": 900
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_1900"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 4500
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_1300"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 8100
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_1400"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 11700
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_1100"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 15300
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_1200"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 18900
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_1000"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 22500
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_2255"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 26100
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_2355"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 29700
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_2000"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 33300
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_2155"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 36900
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_2100"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 40500
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_0455"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 44100
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_0600"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 47700
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_0600"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 51300
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_0601"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 54900
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_0602"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 58500
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_0603"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 62100
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_0604"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 65700
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_0605"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 69300
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_0606"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 72900
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_0607"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 76500
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_0608"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 80100
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_0609"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 83700
            },
            {
              "trip": {
                "gtfsId": "HSL:6173_20161107_Ma_2_0610"
              },
              "serviceDay": 1479679200,
              "realtimeArrival": 87300
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

    elif request_body == '{stop(id: "HSL:4610207") {  name  code  vehicleType  stoptimesForServiceDate(date: "%s"){     pattern {         code         name         directionId         route {             gtfsId             longName             shortName         }     }     stoptimes {         trip{             gtfsId         }         stopHeadsign         serviceDay    	    realtimeArrival      }    }  }}' % (datetime.datetime.now().strftime("%Y%m%d")):
        return re.sub(r'"serviceDay":.*,',
                      '"serviceDay": ' + str(int(time.mktime(time.strptime(datetime.datetime.now().strftime("%Y%m%d"), "%Y%m%d")))) + ",",
            '''
{
    "data": {
        "stop": {
            "code": "V6107", 
            "name": "Tikkurilan matkakesk", 
            "stoptimesForServiceDate": [
                {
                    "pattern": {
                        "code": "HSL:4736A:1:01", 
                        "directionId": 1, 
                        "name": "736A to Urheilutie (HSL:4620209)", 
                        "route": {
                            "gtfsId": "HSL:4736A", 
                            "longName": "Jokiniemi-Tikkurila-Korso-Vierum\u00e4ki", 
                            "shortName": "736A"
                        }
                    }, 
                    "stoptimes": []
                }, 
                {
                    "pattern": {
                        "code": "HSL:4712:0:01", 
                        "directionId": 0, 
                        "name": "712 to Tikkurilan matkakesk (HSL:4610207)", 
                        "route": {
                            "gtfsId": "HSL:4712", 
                            "longName": "Kuninkaanm\u00e4ki-Tikkurila", 
                            "shortName": "712"
                        }
                    }, 
                    "stoptimes": [
                        {
                            "realtimeArrival": 40740, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4712_20161114_Su_1_1102"
                            }
                        }, 
                        {
                            "realtimeArrival": 37080, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4712_20161114_Su_1_1002"
                            }
                        }, 
                        {
                            "realtimeArrival": 22620, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4712_20161114_Su_1_0602"
                            }
                        }, 
                        {
                            "realtimeArrival": 29820, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4712_20161114_Su_1_0802"
                            }
                        }, 
                        {
                            "realtimeArrival": 26220, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4712_20161114_Su_1_0702"
                            }
                        }, 
                        {
                            "realtimeArrival": 33420, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4712_20161114_Su_1_0902"
                            }
                        }, 
                        {
                            "realtimeArrival": 73020, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4712_20161114_Su_1_2002"
                            }
                        }, 
                        {
                            "realtimeArrival": 80220, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4712_20161114_Su_1_2202"
                            }
                        }, 
                        {
                            "realtimeArrival": 76620, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4712_20161114_Su_1_2102"
                            }
                        }, 
                        {
                            "realtimeArrival": 83820, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4712_20161114_Su_1_2302"
                            }
                        }, 
                        {
                            "realtimeArrival": 47940, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4712_20161114_Su_1_1302"
                            }
                        }, 
                        {
                            "realtimeArrival": 44340, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4712_20161114_Su_1_1202"
                            }
                        }, 
                        {
                            "realtimeArrival": 55140, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4712_20161114_Su_1_1502"
                            }
                        }, 
                        {
                            "realtimeArrival": 51540, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4712_20161114_Su_1_1402"
                            }
                        }, 
                        {
                            "realtimeArrival": 62340, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4712_20161114_Su_1_1702"
                            }
                        }, 
                        {
                            "realtimeArrival": 58740, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4712_20161114_Su_1_1602"
                            }
                        }, 
                        {
                            "realtimeArrival": 69480, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4712_20161114_Su_1_1902"
                            }
                        }, 
                        {
                            "realtimeArrival": 65940, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4712_20161114_Su_1_1802"
                            }
                        }
                    ]
                }, 
                {
                    "pattern": {
                        "code": "HSL:4619:1:01", 
                        "directionId": 1, 
                        "name": "619 to Tikkurilan matkakesk (HSL:4610207)", 
                        "route": {
                            "gtfsId": "HSL:4619", 
                            "longName": "Tikkurila-Hiekkaharju-Simonsilta", 
                            "shortName": "619"
                        }
                    }, 
                    "stoptimes": [
                        {
                            "realtimeArrival": 34320, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_0921"
                            }
                        }, 
                        {
                            "realtimeArrival": 36180, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_0951"
                            }
                        }, 
                        {
                            "realtimeArrival": 23160, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_0615"
                            }
                        }, 
                        {
                            "realtimeArrival": 21360, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_0545"
                            }
                        }, 
                        {
                            "realtimeArrival": 30360, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_0815"
                            }
                        }, 
                        {
                            "realtimeArrival": 32160, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_0845"
                            }
                        }, 
                        {
                            "realtimeArrival": 28560, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_0745"
                            }
                        }, 
                        {
                            "realtimeArrival": 26760, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_0715"
                            }
                        }, 
                        {
                            "realtimeArrival": 24960, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_0645"
                            }
                        }, 
                        {
                            "realtimeArrival": 39180, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_1041"
                            }
                        }, 
                        {
                            "realtimeArrival": 37380, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_1011"
                            }
                        }, 
                        {
                            "realtimeArrival": 44640, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_1211"
                            }
                        }, 
                        {
                            "realtimeArrival": 46440, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_1241"
                            }
                        }, 
                        {
                            "realtimeArrival": 40980, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_1111"
                            }
                        }, 
                        {
                            "realtimeArrival": 42840, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_1141"
                            }
                        }, 
                        {
                            "realtimeArrival": 69780, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_1911"
                            }
                        }, 
                        {
                            "realtimeArrival": 71580, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_1941"
                            }
                        }, 
                        {
                            "realtimeArrival": 68040, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_1841"
                            }
                        }, 
                        {
                            "realtimeArrival": 66240, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_1811"
                            }
                        }, 
                        {
                            "realtimeArrival": 64440, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_1741"
                            }
                        }, 
                        {
                            "realtimeArrival": 53640, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_1441"
                            }
                        }, 
                        {
                            "realtimeArrival": 51840, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_1411"
                            }
                        }, 
                        {
                            "realtimeArrival": 50040, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_1341"
                            }
                        }, 
                        {
                            "realtimeArrival": 48240, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_1311"
                            }
                        }, 
                        {
                            "realtimeArrival": 62640, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_1711"
                            }
                        }, 
                        {
                            "realtimeArrival": 59040, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_1611"
                            }
                        }, 
                        {
                            "realtimeArrival": 60840, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_1641"
                            }
                        }, 
                        {
                            "realtimeArrival": 55440, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_1511"
                            }
                        }, 
                        {
                            "realtimeArrival": 57240, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_1541"
                            }
                        }, 
                        {
                            "realtimeArrival": 84360, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_2315"
                            }
                        }, 
                        {
                            "realtimeArrival": 82560, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_2245"
                            }
                        }, 
                        {
                            "realtimeArrival": 80760, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_2215"
                            }
                        }, 
                        {
                            "realtimeArrival": 78720, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_2141"
                            }
                        }, 
                        {
                            "realtimeArrival": 76980, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_2112"
                            }
                        }, 
                        {
                            "realtimeArrival": 75180, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_2041"
                            }
                        }, 
                        {
                            "realtimeArrival": 73380, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4619_20161114_Su_2_2011"
                            }
                        }
                    ]
                }, 
                {
                    "pattern": {
                        "code": "HSL:4724N:1:01", 
                        "directionId": 1, 
                        "name": "724N to Rautatientori (HSL:1020201)", 
                        "route": {
                            "gtfsId": "HSL:4724N", 
                            "longName": "Rautatientori-Tikkurila-Koivukyl\u00e4-P\u00e4iv\u00e4kumpu", 
                            "shortName": "724N"
                        }
                    }, 
                    "stoptimes": [
                        {
                            "realtimeArrival": 23160, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Rautatientori", 
                            "trip": {
                                "gtfsId": "HSL:4724N_20161114_Su_2_0605"
                            }
                        }, 
                        {
                            "realtimeArrival": 26760, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Rautatientori", 
                            "trip": {
                                "gtfsId": "HSL:4724N_20161114_Su_2_0705"
                            }
                        }, 
                        {
                            "realtimeArrival": 84000, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Rautatientori", 
                            "trip": {
                                "gtfsId": "HSL:4724N_20161114_Su_2_2300"
                            }
                        }, 
                        {
                            "realtimeArrival": 87600, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Rautatientori", 
                            "trip": {
                                "gtfsId": "HSL:4724N_20161114_Su_2_2400"
                            }
                        }
                    ]
                }, 
                {
                    "pattern": {
                        "code": "HSL:4711:0:01", 
                        "directionId": 0, 
                        "name": "711 to Tikkurilan matkakesk (HSL:4610207)", 
                        "route": {
                            "gtfsId": "HSL:4711", 
                            "longName": "Kuninkaanm\u00e4ki-Tikkurila", 
                            "shortName": "711"
                        }
                    }, 
                    "stoptimes": [
                        {
                            "realtimeArrival": 31920, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4711_20161114_Su_1_0828"
                            }
                        }, 
                        {
                            "realtimeArrival": 28320, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4711_20161114_Su_1_0728"
                            }
                        }, 
                        {
                            "realtimeArrival": 24720, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4711_20161114_Su_1_0628"
                            }
                        }, 
                        {
                            "realtimeArrival": 35520, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4711_20161114_Su_1_0928"
                            }
                        }, 
                        {
                            "realtimeArrival": 71580, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4711_20161114_Su_1_1928"
                            }
                        }, 
                        {
                            "realtimeArrival": 68040, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4711_20161114_Su_1_1828"
                            }
                        }, 
                        {
                            "realtimeArrival": 46440, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4711_20161114_Su_1_1228"
                            }
                        }, 
                        {
                            "realtimeArrival": 42840, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4711_20161114_Su_1_1128"
                            }
                        }, 
                        {
                            "realtimeArrival": 39180, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4711_20161114_Su_1_1028"
                            }
                        }, 
                        {
                            "realtimeArrival": 64440, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4711_20161114_Su_1_1728"
                            }
                        }, 
                        {
                            "realtimeArrival": 60900, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4711_20161114_Su_1_1628"
                            }
                        }, 
                        {
                            "realtimeArrival": 57300, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4711_20161114_Su_1_1528"
                            }
                        }, 
                        {
                            "realtimeArrival": 53700, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4711_20161114_Su_1_1428"
                            }
                        }, 
                        {
                            "realtimeArrival": 50100, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4711_20161114_Su_1_1328"
                            }
                        }, 
                        {
                            "realtimeArrival": 82260, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4711_20161114_Su_1_2228"
                            }
                        }, 
                        {
                            "realtimeArrival": 78720, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4711_20161114_Su_1_2128"
                            }
                        }, 
                        {
                            "realtimeArrival": 75180, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4711_20161114_Su_1_2028"
                            }
                        }
                    ]
                }, 
                {
                    "pattern": {
                        "code": "HSL:4562:1:02", 
                        "directionId": 1, 
                        "name": "562 to Mellunm\u00e4ki(M) (HSL:1473118) from Aviapolis (HSL:4520269) via Kuminatie (HSL:4630218)", 
                        "route": {
                            "gtfsId": "HSL:4562", 
                            "longName": "Mellunm\u00e4ki-Tikkurila-Aviapolis", 
                            "shortName": "562"
                        }
                    }, 
                    "stoptimes": [
                        {
                            "realtimeArrival": 53640, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1430"
                            }
                        }, 
                        {
                            "realtimeArrival": 54540, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1445"
                            }
                        }, 
                        {
                            "realtimeArrival": 52740, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1415"
                            }
                        }, 
                        {
                            "realtimeArrival": 51840, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1400"
                            }
                        }, 
                        {
                            "realtimeArrival": 55440, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1500"
                            }
                        }, 
                        {
                            "realtimeArrival": 57240, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1530"
                            }
                        }, 
                        {
                            "realtimeArrival": 58140, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1545"
                            }
                        }, 
                        {
                            "realtimeArrival": 56340, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1515"
                            }
                        }, 
                        {
                            "realtimeArrival": 59940, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1615"
                            }
                        }, 
                        {
                            "realtimeArrival": 59040, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1600"
                            }
                        }, 
                        {
                            "realtimeArrival": 60840, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1630"
                            }
                        }, 
                        {
                            "realtimeArrival": 61740, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1645"
                            }
                        }, 
                        {
                            "realtimeArrival": 62640, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1700"
                            }
                        }, 
                        {
                            "realtimeArrival": 64380, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1730"
                            }
                        }, 
                        {
                            "realtimeArrival": 65280, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1745"
                            }
                        }, 
                        {
                            "realtimeArrival": 63480, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1715"
                            }
                        }, 
                        {
                            "realtimeArrival": 67080, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1815"
                            }
                        }, 
                        {
                            "realtimeArrival": 66180, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1800"
                            }
                        }, 
                        {
                            "realtimeArrival": 69120, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1850"
                            }
                        }, 
                        {
                            "realtimeArrival": 67920, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1830"
                            }
                        }, 
                        {
                            "realtimeArrival": 71460, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1930"
                            }
                        }, 
                        {
                            "realtimeArrival": 70320, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1910"
                            }
                        }, 
                        {
                            "realtimeArrival": 72660, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1950"
                            }
                        }, 
                        {
                            "realtimeArrival": 75060, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_2030"
                            }
                        }, 
                        {
                            "realtimeArrival": 73860, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_2010"
                            }
                        }, 
                        {
                            "realtimeArrival": 76140, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_2050"
                            }
                        }, 
                        {
                            "realtimeArrival": 77340, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_2110"
                            }
                        }, 
                        {
                            "realtimeArrival": 79680, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_2150"
                            }
                        }, 
                        {
                            "realtimeArrival": 78540, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_2130"
                            }
                        }, 
                        {
                            "realtimeArrival": 82020, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_2230"
                            }
                        }, 
                        {
                            "realtimeArrival": 80820, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_2210"
                            }
                        }, 
                        {
                            "realtimeArrival": 83220, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_2250"
                            }
                        }, 
                        {
                            "realtimeArrival": 84420, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_2310"
                            }
                        }, 
                        {
                            "realtimeArrival": 86220, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_2340"
                            }
                        }, 
                        {
                            "realtimeArrival": 87960, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_2410"
                            }
                        }, 
                        {
                            "realtimeArrival": 34740, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_0920"
                            }
                        }, 
                        {
                            "realtimeArrival": 33540, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_0900"
                            }
                        }, 
                        {
                            "realtimeArrival": 35940, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_0940"
                            }
                        }, 
                        {
                            "realtimeArrival": 27420, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_0720"
                            }
                        }, 
                        {
                            "realtimeArrival": 26220, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_0700"
                            }
                        }, 
                        {
                            "realtimeArrival": 28620, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_0740"
                            }
                        }, 
                        {
                            "realtimeArrival": 29820, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_0800"
                            }
                        }, 
                        {
                            "realtimeArrival": 32220, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_0840"
                            }
                        }, 
                        {
                            "realtimeArrival": 31020, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_0820"
                            }
                        }, 
                        {
                            "realtimeArrival": 38100, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1015"
                            }
                        }, 
                        {
                            "realtimeArrival": 37140, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1000"
                            }
                        }, 
                        {
                            "realtimeArrival": 39060, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1030"
                            }
                        }, 
                        {
                            "realtimeArrival": 39960, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1045"
                            }
                        }, 
                        {
                            "realtimeArrival": 40860, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1100"
                            }
                        }, 
                        {
                            "realtimeArrival": 42720, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1130"
                            }
                        }, 
                        {
                            "realtimeArrival": 43620, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1145"
                            }
                        }, 
                        {
                            "realtimeArrival": 41760, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1115"
                            }
                        }, 
                        {
                            "realtimeArrival": 45420, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1215"
                            }
                        }, 
                        {
                            "realtimeArrival": 44520, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1200"
                            }
                        }, 
                        {
                            "realtimeArrival": 46380, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1230"
                            }
                        }, 
                        {
                            "realtimeArrival": 47280, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1245"
                            }
                        }, 
                        {
                            "realtimeArrival": 50040, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1330"
                            }
                        }, 
                        {
                            "realtimeArrival": 50940, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1345"
                            }
                        }, 
                        {
                            "realtimeArrival": 49140, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1315"
                            }
                        }, 
                        {
                            "realtimeArrival": 48180, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_2_1300"
                            }
                        }
                    ]
                }, 
                {
                    "pattern": {
                        "code": "HSL:4562:1:01", 
                        "directionId": 1, 
                        "name": "562 to Mellunm\u00e4ki(M) (HSL:1473118) from Aviapolis (HSL:4520269) via Osmank\u00e4\u00e4mintie (HSL:4630211)", 
                        "route": {
                            "gtfsId": "HSL:4562", 
                            "longName": "Mellunm\u00e4ki-Tikkurila-Aviapolis", 
                            "shortName": "562"
                        }
                    }, 
                    "stoptimes": []
                }, 
                {
                    "pattern": {
                        "code": "HSL:4735:1:01", 
                        "directionId": 1, 
                        "name": "735 to Tikkurilan matkakesk (HSL:4610207)", 
                        "route": {
                            "gtfsId": "HSL:4735", 
                            "longName": "Tikkurila-Korso-Mikkola", 
                            "shortName": "735"
                        }
                    }, 
                    "stoptimes": [
                        {
                            "realtimeArrival": 30120, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_0750"
                            }
                        }, 
                        {
                            "realtimeArrival": 33840, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_0850"
                            }
                        }, 
                        {
                            "realtimeArrival": 31980, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_0820"
                            }
                        }, 
                        {
                            "realtimeArrival": 35700, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_0920"
                            }
                        }, 
                        {
                            "realtimeArrival": 37500, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_0950"
                            }
                        }, 
                        {
                            "realtimeArrival": 22020, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_0537"
                            }
                        }, 
                        {
                            "realtimeArrival": 26520, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_0650"
                            }
                        }, 
                        {
                            "realtimeArrival": 24720, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_0620"
                            }
                        }, 
                        {
                            "realtimeArrival": 28320, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_0720"
                            }
                        }, 
                        {
                            "realtimeArrival": 70020, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_1852"
                            }
                        }, 
                        {
                            "realtimeArrival": 71820, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_1922"
                            }
                        }, 
                        {
                            "realtimeArrival": 73620, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_1952"
                            }
                        }, 
                        {
                            "realtimeArrival": 46800, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_1222"
                            }
                        }, 
                        {
                            "realtimeArrival": 48600, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_1252"
                            }
                        }, 
                        {
                            "realtimeArrival": 50400, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_1322"
                            }
                        }, 
                        {
                            "realtimeArrival": 52200, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_1352"
                            }
                        }, 
                        {
                            "realtimeArrival": 39480, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_1022"
                            }
                        }, 
                        {
                            "realtimeArrival": 41280, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_1052"
                            }
                        }, 
                        {
                            "realtimeArrival": 43140, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_1122"
                            }
                        }, 
                        {
                            "realtimeArrival": 45000, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_1152"
                            }
                        }, 
                        {
                            "realtimeArrival": 61140, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_1622"
                            }
                        }, 
                        {
                            "realtimeArrival": 62940, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_1652"
                            }
                        }, 
                        {
                            "realtimeArrival": 64740, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_1722"
                            }
                        }, 
                        {
                            "realtimeArrival": 66480, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_1752"
                            }
                        }, 
                        {
                            "realtimeArrival": 68220, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_1822"
                            }
                        }, 
                        {
                            "realtimeArrival": 54000, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_1422"
                            }
                        }, 
                        {
                            "realtimeArrival": 55800, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_1452"
                            }
                        }, 
                        {
                            "realtimeArrival": 57540, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_1522"
                            }
                        }, 
                        {
                            "realtimeArrival": 59340, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_1552"
                            }
                        }, 
                        {
                            "realtimeArrival": 80520, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_2150"
                            }
                        }, 
                        {
                            "realtimeArrival": 78720, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_2120"
                            }
                        }, 
                        {
                            "realtimeArrival": 82260, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_2220"
                            }
                        }, 
                        {
                            "realtimeArrival": 84060, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_2250"
                            }
                        }, 
                        {
                            "realtimeArrival": 75360, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_2022"
                            }
                        }, 
                        {
                            "realtimeArrival": 77100, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_2052"
                            }
                        }, 
                        {
                            "realtimeArrival": 87660, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4735_20161114_Su_2_2350"
                            }
                        }
                    ]
                }, 
                {
                    "pattern": {
                        "code": "HSL:4711K:0:01", 
                        "directionId": 0, 
                        "name": "711K to Tikkurilan matkakesk (HSL:4610207)", 
                        "route": {
                            "gtfsId": "HSL:4711K", 
                            "longName": "Kuninkaanm\u00e4ki-Sotunki-Tikkurila", 
                            "shortName": "711K"
                        }
                    }, 
                    "stoptimes": []
                }, 
                {
                    "pattern": {
                        "code": "HSL:4624:1:01", 
                        "directionId": 1, 
                        "name": "624 to Tikkurilan matkakesk (HSL:4610207)", 
                        "route": {
                            "gtfsId": "HSL:4624", 
                            "longName": "Tikkurila-Ilola-Leinel\u00e4-Koivukyl\u00e4-Havukoski-P\u00e4iv\u00e4kumpu", 
                            "shortName": "624"
                        }
                    }, 
                    "stoptimes": [
                        {
                            "realtimeArrival": 74160, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_2000"
                            }
                        }, 
                        {
                            "realtimeArrival": 75900, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_2030"
                            }
                        }, 
                        {
                            "realtimeArrival": 86400, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_2330"
                            }
                        }, 
                        {
                            "realtimeArrival": 81120, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_2200"
                            }
                        }, 
                        {
                            "realtimeArrival": 82860, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_2230"
                            }
                        }, 
                        {
                            "realtimeArrival": 79320, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_2130"
                            }
                        }, 
                        {
                            "realtimeArrival": 77520, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_2100"
                            }
                        }, 
                        {
                            "realtimeArrival": 41820, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_1101"
                            }
                        }, 
                        {
                            "realtimeArrival": 43680, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_1131"
                            }
                        }, 
                        {
                            "realtimeArrival": 40020, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_1031"
                            }
                        }, 
                        {
                            "realtimeArrival": 38100, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_1000"
                            }
                        }, 
                        {
                            "realtimeArrival": 58140, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_1532"
                            }
                        }, 
                        {
                            "realtimeArrival": 56340, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_1502"
                            }
                        }, 
                        {
                            "realtimeArrival": 54540, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_1432"
                            }
                        }, 
                        {
                            "realtimeArrival": 52740, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_1402"
                            }
                        }, 
                        {
                            "realtimeArrival": 50880, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_1331"
                            }
                        }, 
                        {
                            "realtimeArrival": 49080, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_1301"
                            }
                        }, 
                        {
                            "realtimeArrival": 45480, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_1201"
                            }
                        }, 
                        {
                            "realtimeArrival": 47280, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_1231"
                            }
                        }, 
                        {
                            "realtimeArrival": 70620, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_1901"
                            }
                        }, 
                        {
                            "realtimeArrival": 72420, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_1931"
                            }
                        }, 
                        {
                            "realtimeArrival": 68760, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_1831"
                            }
                        }, 
                        {
                            "realtimeArrival": 67080, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_1802"
                            }
                        }, 
                        {
                            "realtimeArrival": 65280, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_1732"
                            }
                        }, 
                        {
                            "realtimeArrival": 63540, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_1702"
                            }
                        }, 
                        {
                            "realtimeArrival": 61740, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_1632"
                            }
                        }, 
                        {
                            "realtimeArrival": 59940, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_1602"
                            }
                        }, 
                        {
                            "realtimeArrival": 34380, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_0900"
                            }
                        }, 
                        {
                            "realtimeArrival": 36240, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_0930"
                            }
                        }, 
                        {
                            "realtimeArrival": 30720, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_0800"
                            }
                        }, 
                        {
                            "realtimeArrival": 32520, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_0830"
                            }
                        }, 
                        {
                            "realtimeArrival": 28920, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_0730"
                            }
                        }, 
                        {
                            "realtimeArrival": 25320, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_0630"
                            }
                        }, 
                        {
                            "realtimeArrival": 21660, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624_20161114_Su_2_0530"
                            }
                        }
                    ]
                }, 
                {
                    "pattern": {
                        "code": "HSL:4562N:0:01", 
                        "directionId": 0, 
                        "name": "562N to Lentoasema T2 (HSL:4530212) from Mellunm\u00e4ki(M) (HSL:1473221) via Peltolantori (HSL:4630206)", 
                        "route": {
                            "gtfsId": "HSL:4562N", 
                            "longName": "Mellunm\u00e4ki-Tikkurila-Aviapolis-Lentoasema", 
                            "shortName": "562N"
                        }
                    }, 
                    "stoptimes": [
                        {
                            "realtimeArrival": 19380, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Lentoasema via Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562N_20161201_Su_1_0502"
                            }
                        }, 
                        {
                            "realtimeArrival": 21180, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Lentoasema via Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562N_20161201_Su_1_0532"
                            }
                        }, 
                        {
                            "realtimeArrival": 15780, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Lentoasema via Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562N_20161201_Su_1_0402"
                            }
                        }, 
                        {
                            "realtimeArrival": 17580, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Lentoasema via Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562N_20161201_Su_1_0432"
                            }
                        }, 
                        {
                            "realtimeArrival": 85980, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Lentoasema via Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562N_20161201_Su_1_2332"
                            }
                        }, 
                        {
                            "realtimeArrival": 93180, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Lentoasema via Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562N_20161201_Su_1_2532"
                            }
                        }, 
                        {
                            "realtimeArrival": 91380, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Lentoasema via Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562N_20161201_Su_1_2502"
                            }
                        }, 
                        {
                            "realtimeArrival": 87780, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Lentoasema via Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562N_20161201_Su_1_2402"
                            }
                        }, 
                        {
                            "realtimeArrival": 89580, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Lentoasema via Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562N_20161201_Su_1_2432"
                            }
                        }, 
                        {
                            "realtimeArrival": 98580, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Lentoasema via Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562N_20161201_Su_1_2702"
                            }
                        }, 
                        {
                            "realtimeArrival": 100380, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Lentoasema via Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562N_20161201_Su_1_2732"
                            }
                        }, 
                        {
                            "realtimeArrival": 94980, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Lentoasema via Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562N_20161201_Su_1_2602"
                            }
                        }, 
                        {
                            "realtimeArrival": 96780, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Lentoasema via Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562N_20161201_Su_1_2632"
                            }
                        }
                    ]
                }, 
                {
                    "pattern": {
                        "code": "HSL:4562N:0:02", 
                        "directionId": 0, 
                        "name": "562N to Lentoasema T2 (HSL:4530212) from Mellunm\u00e4ki(M) (HSL:1473221) via Krassitie (HSL:4630233)", 
                        "route": {
                            "gtfsId": "HSL:4562N", 
                            "longName": "Mellunm\u00e4ki-Tikkurila-Aviapolis-Lentoasema", 
                            "shortName": "562N"
                        }
                    }, 
                    "stoptimes": []
                }, 
                {
                    "pattern": {
                        "code": "HSL:4311A:1:01", 
                        "directionId": 1, 
                        "name": "311A to Tikkurilan matkakesk (HSL:4610207)", 
                        "route": {
                            "gtfsId": "HSL:4311A", 
                            "longName": "Tikkurila-Myyrm\u00e4ki-H\u00e4meenkyl\u00e4", 
                            "shortName": "311A"
                        }
                    }, 
                    "stoptimes": []
                }, 
                {
                    "pattern": {
                        "code": "HSL:4576:1:01", 
                        "directionId": 1, 
                        "name": "576 to Tikkurilan matkakesk (HSL:4610207)", 
                        "route": {
                            "gtfsId": "HSL:4576", 
                            "longName": "Tikkurila-Seutula-Kivist\u00f6", 
                            "shortName": "576"
                        }
                    }, 
                    "stoptimes": [
                        {
                            "realtimeArrival": 38280, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4576_20161114_Su_2_0958"
                            }
                        }, 
                        {
                            "realtimeArrival": 34680, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4576_20161114_Su_2_0858"
                            }
                        }, 
                        {
                            "realtimeArrival": 23820, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4576_20161114_Su_2_0558"
                            }
                        }, 
                        {
                            "realtimeArrival": 31020, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4576_20161114_Su_2_0758"
                            }
                        }, 
                        {
                            "realtimeArrival": 27420, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4576_20161114_Su_2_0658"
                            }
                        }, 
                        {
                            "realtimeArrival": 42360, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4576_20161114_Su_2_1105"
                            }
                        }, 
                        {
                            "realtimeArrival": 49560, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4576_20161114_Su_2_1305"
                            }
                        }, 
                        {
                            "realtimeArrival": 53160, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4576_20161114_Su_2_1405"
                            }
                        }, 
                        {
                            "realtimeArrival": 45960, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4576_20161114_Su_2_1205"
                            }
                        }, 
                        {
                            "realtimeArrival": 60420, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4576_20161114_Su_2_1605"
                            }
                        }, 
                        {
                            "realtimeArrival": 56820, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4576_20161114_Su_2_1505"
                            }
                        }, 
                        {
                            "realtimeArrival": 67560, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4576_20161114_Su_2_1805"
                            }
                        }, 
                        {
                            "realtimeArrival": 63960, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4576_20161114_Su_2_1705"
                            }
                        }, 
                        {
                            "realtimeArrival": 71220, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4576_20161114_Su_2_1907"
                            }
                        }, 
                        {
                            "realtimeArrival": 74820, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4576_20161114_Su_2_2007"
                            }
                        }, 
                        {
                            "realtimeArrival": 81960, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4576_20161114_Su_2_2207"
                            }
                        }, 
                        {
                            "realtimeArrival": 78360, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4576_20161114_Su_2_2107"
                            }
                        }, 
                        {
                            "realtimeArrival": 86100, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4576_20161114_Su_2_2317"
                            }
                        }
                    ]
                }, 
                {
                    "pattern": {
                        "code": "HSL:4611:0:01", 
                        "directionId": 0, 
                        "name": "611 to Tikkurilan matkakesk (HSL:4610207)", 
                        "route": {
                            "gtfsId": "HSL:4611", 
                            "longName": "Rautatientori-Siltam\u00e4ki-Suutarila-Tikkurila", 
                            "shortName": "611"
                        }
                    }, 
                    "stoptimes": []
                }, 
                {
                    "pattern": {
                        "code": "HSL:4736A:0:01", 
                        "directionId": 0, 
                        "name": "736A to Ruokkitie (HSL:4870209)", 
                        "route": {
                            "gtfsId": "HSL:4736A", 
                            "longName": "Jokiniemi-Tikkurila-Korso-Vierum\u00e4ki", 
                            "shortName": "736A"
                        }
                    }, 
                    "stoptimes": []
                }, 
                {
                    "pattern": {
                        "code": "HSL:4631:1:01", 
                        "directionId": 1, 
                        "name": "631 to Tikkurilan matkakesk (HSL:4610207)", 
                        "route": {
                            "gtfsId": "HSL:4631", 
                            "longName": "Tikkurila-Kulom\u00e4ki", 
                            "shortName": "631"
                        }
                    }, 
                    "stoptimes": [
                        {
                            "realtimeArrival": 89400, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_2424"
                            }
                        }, 
                        {
                            "realtimeArrival": 75240, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_2022"
                            }
                        }, 
                        {
                            "realtimeArrival": 76980, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_2052"
                            }
                        }, 
                        {
                            "realtimeArrival": 80460, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_2152"
                            }
                        }, 
                        {
                            "realtimeArrival": 78660, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_2122"
                            }
                        }, 
                        {
                            "realtimeArrival": 82380, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_2224"
                            }
                        }, 
                        {
                            "realtimeArrival": 85800, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_2324"
                            }
                        }, 
                        {
                            "realtimeArrival": 28140, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_0722"
                            }
                        }, 
                        {
                            "realtimeArrival": 31860, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_0822"
                            }
                        }, 
                        {
                            "realtimeArrival": 33720, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_0852"
                            }
                        }, 
                        {
                            "realtimeArrival": 30000, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_0752"
                            }
                        }, 
                        {
                            "realtimeArrival": 35640, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_0922"
                            }
                        }, 
                        {
                            "realtimeArrival": 37500, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_0952"
                            }
                        }, 
                        {
                            "realtimeArrival": 24600, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_0624"
                            }
                        }, 
                        {
                            "realtimeArrival": 44760, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_1152"
                            }
                        }, 
                        {
                            "realtimeArrival": 42960, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_1122"
                            }
                        }, 
                        {
                            "realtimeArrival": 46560, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_1222"
                            }
                        }, 
                        {
                            "realtimeArrival": 48360, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_1252"
                            }
                        }, 
                        {
                            "realtimeArrival": 51960, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_1352"
                            }
                        }, 
                        {
                            "realtimeArrival": 50160, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_1322"
                            }
                        }, 
                        {
                            "realtimeArrival": 55560, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_1452"
                            }
                        }, 
                        {
                            "realtimeArrival": 53760, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_1422"
                            }
                        }, 
                        {
                            "realtimeArrival": 41160, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_1052"
                            }
                        }, 
                        {
                            "realtimeArrival": 39360, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_1022"
                            }
                        }, 
                        {
                            "realtimeArrival": 59160, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_1552"
                            }
                        }, 
                        {
                            "realtimeArrival": 57360, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_1522"
                            }
                        }, 
                        {
                            "realtimeArrival": 60960, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_1622"
                            }
                        }, 
                        {
                            "realtimeArrival": 62760, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_1652"
                            }
                        }, 
                        {
                            "realtimeArrival": 68100, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_1822"
                            }
                        }, 
                        {
                            "realtimeArrival": 66360, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_1752"
                            }
                        }, 
                        {
                            "realtimeArrival": 64560, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_1722"
                            }
                        }, 
                        {
                            "realtimeArrival": 73440, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_1952"
                            }
                        }, 
                        {
                            "realtimeArrival": 71640, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_1922"
                            }
                        }, 
                        {
                            "realtimeArrival": 69900, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4631_20161114_Su_2_1852"
                            }
                        }
                    ]
                }, 
                {
                    "pattern": {
                        "code": "HSL:4736:1:01", 
                        "directionId": 1, 
                        "name": "736 to Tikkurilan matkakesk (HSL:4610207)", 
                        "route": {
                            "gtfsId": "HSL:4736", 
                            "longName": "Tikkurila-Vierum\u00e4ki", 
                            "shortName": "736"
                        }
                    }, 
                    "stoptimes": [
                        {
                            "realtimeArrival": 25740, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4736_20161114_Su_2_0620"
                            }
                        }, 
                        {
                            "realtimeArrival": 29340, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4736_20161114_Su_2_0720"
                            }
                        }, 
                        {
                            "realtimeArrival": 32940, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4736_20161114_Su_2_0820"
                            }
                        }, 
                        {
                            "realtimeArrival": 36660, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4736_20161114_Su_2_0920"
                            }
                        }, 
                        {
                            "realtimeArrival": 40260, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4736_20161114_Su_2_1020"
                            }
                        }, 
                        {
                            "realtimeArrival": 43920, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4736_20161114_Su_2_1120"
                            }
                        }, 
                        {
                            "realtimeArrival": 47640, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4736_20161114_Su_2_1220"
                            }
                        }, 
                        {
                            "realtimeArrival": 51240, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4736_20161114_Su_2_1320"
                            }
                        }, 
                        {
                            "realtimeArrival": 54840, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4736_20161114_Su_2_1420"
                            }
                        }, 
                        {
                            "realtimeArrival": 58440, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4736_20161114_Su_2_1520"
                            }
                        }, 
                        {
                            "realtimeArrival": 61980, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4736_20161114_Su_2_1620"
                            }
                        }, 
                        {
                            "realtimeArrival": 65520, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4736_20161114_Su_2_1720"
                            }
                        }, 
                        {
                            "realtimeArrival": 69120, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4736_20161114_Su_2_1820"
                            }
                        }, 
                        {
                            "realtimeArrival": 72720, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4736_20161114_Su_2_1920"
                            }
                        }, 
                        {
                            "realtimeArrival": 76320, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4736_20161114_Su_2_2020"
                            }
                        }, 
                        {
                            "realtimeArrival": 79680, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4736_20161114_Su_2_2120"
                            }
                        }, 
                        {
                            "realtimeArrival": 83220, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4736_20161114_Su_2_2220"
                            }
                        }, 
                        {
                            "realtimeArrival": 86820, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4736_20161114_Su_2_2320"
                            }
                        }
                    ]
                }, 
                {
                    "pattern": {
                        "code": "HSL:4562N:1:01", 
                        "directionId": 1, 
                        "name": "562N to Mellunm\u00e4ki(M) (HSL:1473118) from Lentoasema T1 (HSL:4530213) via Kuminatie (HSL:4630218)", 
                        "route": {
                            "gtfsId": "HSL:4562N", 
                            "longName": "Mellunm\u00e4ki-Tikkurila-Aviapolis-Lentoasema", 
                            "shortName": "562N"
                        }
                    }, 
                    "stoptimes": [
                        {
                            "realtimeArrival": 93420, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki via Hakunila", 
                            "trip": {
                                "gtfsId": "HSL:4562N_20161201_Su_2_2535"
                            }
                        }, 
                        {
                            "realtimeArrival": 91620, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki via Hakunila", 
                            "trip": {
                                "gtfsId": "HSL:4562N_20161201_Su_2_2505"
                            }
                        }, 
                        {
                            "realtimeArrival": 89820, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki via Hakunila", 
                            "trip": {
                                "gtfsId": "HSL:4562N_20161201_Su_2_2435"
                            }
                        }, 
                        {
                            "realtimeArrival": 100620, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki via Hakunila", 
                            "trip": {
                                "gtfsId": "HSL:4562N_20161201_Su_2_2735"
                            }
                        }, 
                        {
                            "realtimeArrival": 98820, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki via Hakunila", 
                            "trip": {
                                "gtfsId": "HSL:4562N_20161201_Su_2_2705"
                            }
                        }, 
                        {
                            "realtimeArrival": 97020, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki via Hakunila", 
                            "trip": {
                                "gtfsId": "HSL:4562N_20161201_Su_2_2635"
                            }
                        }, 
                        {
                            "realtimeArrival": 95220, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki via Hakunila", 
                            "trip": {
                                "gtfsId": "HSL:4562N_20161201_Su_2_2605"
                            }
                        }, 
                        {
                            "realtimeArrival": 21480, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki via Hakunila", 
                            "trip": {
                                "gtfsId": "HSL:4562N_20161201_Su_2_0535"
                            }
                        }, 
                        {
                            "realtimeArrival": 19680, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki via Hakunila", 
                            "trip": {
                                "gtfsId": "HSL:4562N_20161201_Su_2_0505"
                            }
                        }, 
                        {
                            "realtimeArrival": 17880, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki via Hakunila", 
                            "trip": {
                                "gtfsId": "HSL:4562N_20161201_Su_2_0435"
                            }
                        }, 
                        {
                            "realtimeArrival": 16020, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki via Hakunila", 
                            "trip": {
                                "gtfsId": "HSL:4562N_20161201_Su_2_0405"
                            }
                        }, 
                        {
                            "realtimeArrival": 25080, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki via Hakunila", 
                            "trip": {
                                "gtfsId": "HSL:4562N_20161201_Su_2_0635"
                            }
                        }, 
                        {
                            "realtimeArrival": 23280, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Mellunm\u00e4ki via Hakunila", 
                            "trip": {
                                "gtfsId": "HSL:4562N_20161201_Su_2_0605"
                            }
                        }
                    ]
                }, 
                {
                    "pattern": {
                        "code": "HSL:4562N:1:02", 
                        "directionId": 1, 
                        "name": "562N to Mellunm\u00e4ki(M) (HSL:1473118) from Lentoasema T1 (HSL:4530213) via Osmank\u00e4\u00e4mintie (HSL:4630211)", 
                        "route": {
                            "gtfsId": "HSL:4562N", 
                            "longName": "Mellunm\u00e4ki-Tikkurila-Aviapolis-Lentoasema", 
                            "shortName": "562N"
                        }
                    }, 
                    "stoptimes": []
                }, 
                {
                    "pattern": {
                        "code": "HSL:4571:1:01", 
                        "directionId": 1, 
                        "name": "571 to Tikkurilan matkakesk (HSL:4610207)", 
                        "route": {
                            "gtfsId": "HSL:4571", 
                            "longName": "Tikkurila-Myyrm\u00e4ki-Varisto", 
                            "shortName": "571"
                        }
                    }, 
                    "stoptimes": [
                        {
                            "realtimeArrival": 76380, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_2017"
                            }
                        }, 
                        {
                            "realtimeArrival": 78060, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_2047"
                            }
                        }, 
                        {
                            "realtimeArrival": 88680, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_2347"
                            }
                        }, 
                        {
                            "realtimeArrival": 86880, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_2317"
                            }
                        }, 
                        {
                            "realtimeArrival": 85080, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_2247"
                            }
                        }, 
                        {
                            "realtimeArrival": 83280, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_2217"
                            }
                        }, 
                        {
                            "realtimeArrival": 79740, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_2117"
                            }
                        }, 
                        {
                            "realtimeArrival": 81480, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_2147"
                            }
                        }, 
                        {
                            "realtimeArrival": 74580, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_1947"
                            }
                        }, 
                        {
                            "realtimeArrival": 72840, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_1917"
                            }
                        }, 
                        {
                            "realtimeArrival": 71100, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_1847"
                            }
                        }, 
                        {
                            "realtimeArrival": 69360, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_1817"
                            }
                        }, 
                        {
                            "realtimeArrival": 66000, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_1717"
                            }
                        }, 
                        {
                            "realtimeArrival": 67800, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_1747"
                            }
                        }, 
                        {
                            "realtimeArrival": 46200, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_1147"
                            }
                        }, 
                        {
                            "realtimeArrival": 44340, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_1117"
                            }
                        }, 
                        {
                            "realtimeArrival": 42360, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_1044"
                            }
                        }, 
                        {
                            "realtimeArrival": 40440, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_1014"
                            }
                        }, 
                        {
                            "realtimeArrival": 64200, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_1647"
                            }
                        }, 
                        {
                            "realtimeArrival": 62400, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_1617"
                            }
                        }, 
                        {
                            "realtimeArrival": 60600, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_1547"
                            }
                        }, 
                        {
                            "realtimeArrival": 58800, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_1517"
                            }
                        }, 
                        {
                            "realtimeArrival": 57060, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_1447"
                            }
                        }, 
                        {
                            "realtimeArrival": 55260, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_1417"
                            }
                        }, 
                        {
                            "realtimeArrival": 51660, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_1317"
                            }
                        }, 
                        {
                            "realtimeArrival": 53460, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_1347"
                            }
                        }, 
                        {
                            "realtimeArrival": 49860, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_1247"
                            }
                        }, 
                        {
                            "realtimeArrival": 48000, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_1217"
                            }
                        }, 
                        {
                            "realtimeArrival": 31140, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_0748"
                            }
                        }, 
                        {
                            "realtimeArrival": 27900, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_0656"
                            }
                        }, 
                        {
                            "realtimeArrival": 24300, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_0556"
                            }
                        }, 
                        {
                            "realtimeArrival": 20700, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_0456"
                            }
                        }, 
                        {
                            "realtimeArrival": 38580, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_0944"
                            }
                        }, 
                        {
                            "realtimeArrival": 36660, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_0917"
                            }
                        }, 
                        {
                            "realtimeArrival": 34800, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_0848"
                            }
                        }, 
                        {
                            "realtimeArrival": 33000, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4571_20161114_Su_2_0818"
                            }
                        }
                    ]
                }, 
                {
                    "pattern": {
                        "code": "HSL:4624N:1:01", 
                        "directionId": 1, 
                        "name": "624N to Tikkurilan matkakesk (HSL:4610207)", 
                        "route": {
                            "gtfsId": "HSL:4624N", 
                            "longName": "Tikkurila-Ruskeasanta-Ilola-Leinel\u00e4", 
                            "shortName": "624N"
                        }
                    }, 
                    "stoptimes": [
                        {
                            "realtimeArrival": 90180, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": null, 
                            "trip": {
                                "gtfsId": "HSL:4624N_20161115_Su_2_2445"
                            }
                        }
                    ]
                }, 
                {
                    "pattern": {
                        "code": "HSL:4562:0:01", 
                        "directionId": 0, 
                        "name": "562 to Aviapolis (HSL:4520266) from Mellunm\u00e4ki(M) (HSL:1473221) via Krassitie (HSL:4630233)", 
                        "route": {
                            "gtfsId": "HSL:4562", 
                            "longName": "Mellunm\u00e4ki-Tikkurila-Aviapolis", 
                            "shortName": "562"
                        }
                    }, 
                    "stoptimes": []
                }, 
                {
                    "pattern": {
                        "code": "HSL:4562:0:02", 
                        "directionId": 0, 
                        "name": "562 to Aviapolis (HSL:4520266) from Mellunm\u00e4ki(M) (HSL:1473221) via Peltolantori (HSL:4630206)", 
                        "route": {
                            "gtfsId": "HSL:4562", 
                            "longName": "Mellunm\u00e4ki-Tikkurila-Aviapolis", 
                            "shortName": "562"
                        }
                    }, 
                    "stoptimes": [
                        {
                            "realtimeArrival": 25440, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_0642"
                            }
                        }, 
                        {
                            "realtimeArrival": 24240, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_0622"
                            }
                        }, 
                        {
                            "realtimeArrival": 23040, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_0602"
                            }
                        }, 
                        {
                            "realtimeArrival": 26640, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_0702"
                            }
                        }, 
                        {
                            "realtimeArrival": 29040, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_0742"
                            }
                        }, 
                        {
                            "realtimeArrival": 27840, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_0722"
                            }
                        }, 
                        {
                            "realtimeArrival": 31500, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_0822"
                            }
                        }, 
                        {
                            "realtimeArrival": 30240, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_0802"
                            }
                        }, 
                        {
                            "realtimeArrival": 32700, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_0842"
                            }
                        }, 
                        {
                            "realtimeArrival": 36420, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_0942"
                            }
                        }, 
                        {
                            "realtimeArrival": 35160, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_0922"
                            }
                        }, 
                        {
                            "realtimeArrival": 33960, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_0902"
                            }
                        }, 
                        {
                            "realtimeArrival": 76620, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_2052"
                            }
                        }, 
                        {
                            "realtimeArrival": 75420, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_2032"
                            }
                        }, 
                        {
                            "realtimeArrival": 74340, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_2012"
                            }
                        }, 
                        {
                            "realtimeArrival": 80100, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_2152"
                            }
                        }, 
                        {
                            "realtimeArrival": 79020, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_2132"
                            }
                        }, 
                        {
                            "realtimeArrival": 77820, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_2112"
                            }
                        }, 
                        {
                            "realtimeArrival": 83580, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_2252"
                            }
                        }, 
                        {
                            "realtimeArrival": 82440, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_2232"
                            }
                        }, 
                        {
                            "realtimeArrival": 81300, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_2212"
                            }
                        }, 
                        {
                            "realtimeArrival": 84780, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_2312"
                            }
                        }, 
                        {
                            "realtimeArrival": 46800, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1232"
                            }
                        }, 
                        {
                            "realtimeArrival": 45900, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1217"
                            }
                        }, 
                        {
                            "realtimeArrival": 45000, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1202"
                            }
                        }, 
                        {
                            "realtimeArrival": 47700, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1247"
                            }
                        }, 
                        {
                            "realtimeArrival": 51420, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1347"
                            }
                        }, 
                        {
                            "realtimeArrival": 50460, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1332"
                            }
                        }, 
                        {
                            "realtimeArrival": 49500, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1317"
                            }
                        }, 
                        {
                            "realtimeArrival": 48600, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1302"
                            }
                        }, 
                        {
                            "realtimeArrival": 55020, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1447"
                            }
                        }, 
                        {
                            "realtimeArrival": 54120, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1432"
                            }
                        }, 
                        {
                            "realtimeArrival": 53220, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1417"
                            }
                        }, 
                        {
                            "realtimeArrival": 52320, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1402"
                            }
                        }, 
                        {
                            "realtimeArrival": 58620, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1547"
                            }
                        }, 
                        {
                            "realtimeArrival": 57720, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1532"
                            }
                        }, 
                        {
                            "realtimeArrival": 56820, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1517"
                            }
                        }, 
                        {
                            "realtimeArrival": 55920, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1502"
                            }
                        }, 
                        {
                            "realtimeArrival": 62220, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1647"
                            }
                        }, 
                        {
                            "realtimeArrival": 61320, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1632"
                            }
                        }, 
                        {
                            "realtimeArrival": 60420, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1617"
                            }
                        }, 
                        {
                            "realtimeArrival": 59520, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1602"
                            }
                        }, 
                        {
                            "realtimeArrival": 65820, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1747"
                            }
                        }, 
                        {
                            "realtimeArrival": 64920, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1732"
                            }
                        }, 
                        {
                            "realtimeArrival": 64020, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1717"
                            }
                        }, 
                        {
                            "realtimeArrival": 63120, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1702"
                            }
                        }, 
                        {
                            "realtimeArrival": 69600, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1852"
                            }
                        }, 
                        {
                            "realtimeArrival": 68460, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1832"
                            }
                        }, 
                        {
                            "realtimeArrival": 67620, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1817"
                            }
                        }, 
                        {
                            "realtimeArrival": 66720, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1802"
                            }
                        }, 
                        {
                            "realtimeArrival": 70800, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1912"
                            }
                        }, 
                        {
                            "realtimeArrival": 73140, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1952"
                            }
                        }, 
                        {
                            "realtimeArrival": 71940, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1932"
                            }
                        }, 
                        {
                            "realtimeArrival": 40320, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1047"
                            }
                        }, 
                        {
                            "realtimeArrival": 39420, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1032"
                            }
                        }, 
                        {
                            "realtimeArrival": 38520, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1017"
                            }
                        }, 
                        {
                            "realtimeArrival": 37620, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1002"
                            }
                        }, 
                        {
                            "realtimeArrival": 42180, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1117"
                            }
                        }, 
                        {
                            "realtimeArrival": 41280, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1102"
                            }
                        }, 
                        {
                            "realtimeArrival": 44100, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1147"
                            }
                        }, 
                        {
                            "realtimeArrival": 43140, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "Aviapolis", 
                            "trip": {
                                "gtfsId": "HSL:4562_20161201_Su_1_1132"
                            }
                        }
                    ]
                }, 
                {
                    "pattern": {
                        "code": "HSL:4612:1:01", 
                        "directionId": 1, 
                        "name": "612 to Tikkurilan matkakesk (HSL:4610207)", 
                        "route": {
                            "gtfsId": "HSL:4612", 
                            "longName": "Tikkurila-Tammisto", 
                            "shortName": "612"
                        }
                    }, 
                    "stoptimes": []
                }, 
                {
                    "pattern": {
                        "code": "HSL:4724N:0:01", 
                        "directionId": 0, 
                        "name": "724N to P\u00e4iv\u00e4kummuntie (HSL:4750222)", 
                        "route": {
                            "gtfsId": "HSL:4724N", 
                            "longName": "Rautatientori-Tikkurila-Koivukyl\u00e4-P\u00e4iv\u00e4kumpu", 
                            "shortName": "724N"
                        }
                    }, 
                    "stoptimes": [
                        {
                            "realtimeArrival": 88380, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "P\u00e4iv\u00e4kumpu via Koivukyl\u00e4", 
                            "trip": {
                                "gtfsId": "HSL:4724N_20161114_Su_1_2405"
                            }
                        }, 
                        {
                            "realtimeArrival": 91920, 
                            "serviceDay": 1480802400, 
                            "stopHeadsign": "P\u00e4iv\u00e4kumpu via Koivukyl\u00e4", 
                            "trip": {
                                "gtfsId": "HSL:4724N_20161114_Su_1_2505"
                            }
                        }
                    ]
                }
            ], 
            "vehicleType": 3
        }
    }
}
        ''')

    elif request_body == '{stop(id: "INVALID") {  name  code  vehicleType  stoptimesForServiceDate(date: "%s"){     pattern {         code         name         directionId         route {             gtfsId             longName             shortName         }     }     stoptimes {         trip{             gtfsId         }         stopHeadsign         serviceDay    	    realtimeArrival      }    }  }}' % (datetime.datetime.now().strftime("%Y%m%d")):
        return '{"data": { "stop": null } }'

    elif request_body == '{trip(id: "INVALID") { stoptimesForDate(serviceDay: "%s") {      stop{          gtfsId          name          code }      serviceDay      realtimeArrival        }       }      }}' % (datetime.datetime.now().strftime("%Y%m%d")):
        return '{"data": { "trip": null } }'

    elif request_body == '''{fuzzyTrip(route:"1", date:"20161204", time:1000, direction:1){
                        gtfsId
                        tripHeadsign
                        route{
                            shortName
                        }
                    }
                }''':
        return '{"data":{"fuzzyTrip":{"gtfsId":"1234", "tripHeadsign":"test", "route":{"shortName":"10"} }}}'

    elif request_body == '{ stops(name:"V6147") { gtfsId code name platformCode lat lon } }':
        return '''
{
  "data": {
    "stops": [
      {
        "gtfsId": "HSL:4610245",
        "code": "V6145",
        "name": "Tikkurilan matkakesk",
        "platformCode": "5",
        "lat": 60.29357090000206,
        "lon": 25.044249799999996
      }
    ]
  }
}'''

    else:
        print("Unhandled query:", request_body)
        return '{"errors": [{"message":"your mock call didn\'t match any request body"}]}'


if __name__ == '__main__':
    print("Starting...")
    serve(app, host='0.0.0.0', port=11111)
