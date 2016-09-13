import os
import datetime

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT', '5000'))

class Foo:

    def hello(self):
        return 'foo'

class DigitransitAPIService:
    def __init__(self):
        self.url = 'http://api.digitransit.fi/routing/v1/routers/hsl/index/graphql'
        #datetime.datetime.now().strftime("%Y%m%d")

    def get_stops(self):
        return ''

    def _get_stops_near_coordinates(self):
        return ''

    def _get_busses_by_stop_id(self):
        return ''