import unittest
import stop
from flask import json, jsonify


class TestStopRoutes(unittest.TestCase):

    def setUp(self):
        stop.app.config['TESTING'] = True
        self.app = stop.app.test_client()

    def test_hello(self):
        self.assertEqual('foo', 'foo')

    def test_stops_get(self):
        response = self.app.get('/stops?lat=1.0&lon=2.0')
        data = json.loads(response.data)
        self.assertEquals(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
