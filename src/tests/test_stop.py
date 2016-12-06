import unittest
import stop


class TestStopRoutes(unittest.TestCase):

    def setUp(self):
        stop.app.config['TESTING'] = True
        self.app = stop.app.test_client()

    def test_stops_get(self):
        response = self.app.get('/stops?lat=1.0&lon=2.0')
        self.assertEqual(response.status_code, 200)

    def test_unicode_destination_name(self):
        response = self.app.get('/stops?lat=60.19255&lon=24.94461')
        self.assertTrue(response.data.find(b"L\\u00e4nsiterminaali") != -1)

    def test_stopsrequests_post(self):
        json_string = '{"trip_id": "1234", "stop_id": "HSL:1282106", "device_id": "123", "push_notification": false}'
        response = self.app.post('/stoprequests', data=json_string, content_type='application/json')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
