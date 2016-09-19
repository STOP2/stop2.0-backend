import os
from flask import Flask
from flask import request
from flask import json

from src import services

app = Flask(__name__)

digitransitAPIService = services.DigitransitAPIService()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def digitransitTest():
    return digitransitAPIService.get_stops(0, 0)


@app.route('/stops', methods=['GET'])
def get_stops():
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    # TODO use service to get json and return it
    result = {}
    result['lat'] = lat
    result['lon'] = lon
    return json.dumps(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT', '5000'))

