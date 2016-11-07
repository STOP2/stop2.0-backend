import json


class DigitransitAPIServiceStub:
    def __init__(self, db):
        self.db = db    # Is not used currently
        self.MQTT_host = "epsilon.fixme.fi"

    def get_stops(self, lon, lat, radius=160):
        if lon == 60.203978 and lat == 24.9633573:
            return json.loads('{"stops": [{"stop": {"schedule": [{"arrival": 5, "destination": "Viikki", "line": "506", "route_id": "HSL:1506", "trip_id": "HSL:1506_20161003_Ma_2_1543", "vehicle_type": 3}, {"arrival": 13, "destination": "Rautatientori", "line": "55", "route_id": "HSL:1055", "trip_id": "HSL:1055_20161003_Ma_2_1611", "vehicle_type": 3}, {"arrival": 17, "destination": "Viikki", "line": "506", "route_id": "HSL:1506", "trip_id": "HSL:1506_20161003_Ma_2_1555", "vehicle_type": 3}, {"arrival": 27, "destination": "Rautatientori", "line": "55", "route_id": "HSL:1055", "trip_id": "HSL:1055_20161003_Ma_2_1626", "vehicle_type": 3}, {"arrival": 30, "destination": "Viikki", "line": "506", "route_id": "HSL:1506", "trip_id": "HSL:1506_20161003_Ma_2_1608", "vehicle_type": 3}], "stop_code": "3597", "stop_name": "A.I. Virtasen aukio"}}]}')
        return json.loads('{"stops": []}')

    def get_stops_near_coordinates(self, lon, lat, radius=160):
        if lon == 60.203978 and lat == 24.9633573:
            if radius >= 300:
                return json.loads('["HSL:1240133", "HSL:1240118", "HSL:1240103"]')
            elif radius >= 150:
                return json.loads('["HSL:1240133"]')
        return json.loads('[]')

    def get_busses_by_stop_id(self, stop_id):
        if stop_id == "HSL:1362141":
            return json.loads('{"schedule": [{"arrival": 2, "destination": "Nissas", "line": "718", "route_id": "HSL:4718", "trip_id": "HSL:4718_20161003_Ma_1_1654", "vehicle_type": 3}, {"arrival": 2, "destination": "Jakom\u00e4ki", "line": "77", "route_id": "HSL:1077", "trip_id": "HSL:1077_20161003_Ma_1_1654", "vehicle_type": 3}, {"arrival": 2, "destination": "Havukoski", "line": "722", "route_id": "HSL:4722", "trip_id": "HSL:4722_20161024_Ma_1_1655", "vehicle_type": 3}, {"arrival": 4, "destination": "Pornainen", "line": "787", "route_id": "HSL:9787", "trip_id": "HSL:9787_20161022_Ma_1_1700", "vehicle_type": 3}, {"arrival": 6, "destination": "Sotunki", "line": "717A", "route_id": "HSL:4717A", "trip_id": "HSL:4717A_20161003_Ma_1_1700", "vehicle_type": 3}, {"arrival": 8, "destination": "Nikinm\u00e4ki", "line": "739", "route_id": "HSL:4739", "trip_id": "HSL:4739_20161024_Ma_1_1700", "vehicle_type": 3}, {"arrival": 11, "destination": "Jakom\u00e4ki", "line": "77", "route_id": "HSL:1077", "trip_id": "HSL:1077_20161003_Ma_1_1704", "vehicle_type": 3}, {"arrival": 14, "destination": "Nikkil\u00e4", "line": "785K", "route_id": "HSL:9785K", "trip_id": "HSL:9785K_20161022_Ma_1_1710", "vehicle_type": 3}, {"arrival": 16, "destination": "Nissas", "line": "718", "route_id": "HSL:4718", "trip_id": "HSL:4718_20161003_Ma_1_1709", "vehicle_type": 3}, {"arrival": 16, "destination": "P\u00e4iv\u00e4kumpu", "line": "724", "route_id": "HSL:4724", "trip_id": "HSL:4724_20161024_Ma_1_1710", "vehicle_type": 3}], "stop_code": "3035", "stop_name": "Viikki"}')
        return json.loads('{}')

    def get_stops_by_trip_id(self, trip_id, stop_code):
        if trip_id == "HSL:3001K_20161003_Ma_1_1156" and stop_code == "V0811":
            return json.loads('{"stops": [{"arrives_in": -309, "stop_code": "V0811", "stop_name": "Korso"}, {"arrives_in": -306, "stop_code": "Ke0091", "stop_name": "Savio"}, {"arrives_in": -302, "stop_code": "Ke0041", "stop_name": "Kerava"}]}')
        return json.loads('{"stops": []}')

    def make_request(self, jsonData):
        return ''