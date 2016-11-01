import os
import json
from flask import Flask
from flask import make_response
from flask import request
from flask import json
from waitress import serve

import services
import db


app = Flask(__name__)

db = db.Database()
digitransitAPIService = services.DigitransitAPIService(db)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test')
def digitransit_test():
    return json.dumps(digitransitAPIService.get_stops(60.203978, 24.9633573))


@app.route('/stoprequests', methods=['POST'])
def stoprequest():
    json_data = request.json
    resp = make_response(json.dumps(digitransitAPIService.make_request(json_data)))
    resp.mimetype = 'application/json'
    return resp

@app.route('/stoprequests/cancel', methods=['POST'])
def stoprequests_cancel():
    request_id = int(request.args.get('request_id'))
    result = digitransitAPIService.cancel_request(request_id)
    return result

@app.route('/stoprequests/report', methods=['POST'])
def report():
    json_data = request.json
    result = digitransitAPIService.store_report(json_data)
    return result

@app.route('/stops', methods=['GET'])
def stops():
    lat = float(request.args.get('lat'))
    lon = float(request.args.get('lon'))
    rad = float(request.args.get('rad', default=160))
    result = digitransitAPIService.get_stops(lat, lon, rad)
    resp = make_response(json.dumps(result))
    resp.mimetype = 'application/json'
    return resp

@app.route('/routes', methods=['GET'])
def routes():
    trip_id = request.args.get('trip_id')
    stop_id = request.args.get('stop_id')
    result = digitransitAPIService.get_stops_by_trip_id(trip_id, stop_id)
    resp = make_response(json.dumps(result))
    resp.mimetype = 'application/json'
    return resp

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=os.getenv('PORT', 5000))
    # app.run(host='0.0.0.0', port=os.getenv('PORT', '5000'))
