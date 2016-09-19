import os
from flask import Flask
from flask import request
from flask import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


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
