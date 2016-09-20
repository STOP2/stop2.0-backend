import os
import json
from flask import Flask
from flask import request
from flask import json
import paho.mqtt.publish as publish

import services


app = Flask(__name__)

digitransitAPIService = services.DigitransitAPIService()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test')
def digitransit_test():
    return json.dumps(digitransitAPIService.get_stops(60.203978, 24.9633573))

@app.route('/stoprequests', methods=['POST'])
def stoprequest():
    testData = '{"bus_id": "1234", "stop_id": "56789", "request_type": "stop"}'
    data = json.loads(testData)
    bus_id = data["bus_id"]
    del data["bus_id"]
    data = json.dumps(data)
    publish.single(topic="stoprequests/"+bus_id, payload=data, hostname="epsilon.fixme.fi")
    return ""

@app.route('/stops', methods=['GET'])
def stops():
    lat = float(request.args.get('lat'))
    lon = float(request.args.get('lon'))
    result = digitransitAPIService.get_stops(lat, lon)
    return json.dumps(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT', '5000'))

