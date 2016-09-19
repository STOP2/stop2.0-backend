import os
import json

from flask import Flask

from src import services


app = Flask(__name__)

digitransitAPIService = services.DigitransitAPIService()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def digitransitTest():
    return json.dumps(digitransitAPIService.get_stops(60.203978,24.9633573))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT', '5000'))


class Foo:

    def hello(self):
        return 'foo'

