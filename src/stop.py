import os

from flask import Flask

from src import services

app = Flask(__name__)

digitransitAPIService = services.DigitransitAPIService()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def digitransitTest():
    return digitransitAPIService.get_busses_by_stop_id("HSL:1362141")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT', '5000'))


class Foo:

    def hello(self):
        return 'foo'

