import unittest
import services
import db
import tests.mock.mock_push_service as mock_push_service


class TestDigitransitAPIService(unittest.TestCase):

    def setUp(self):
        self.digitransitAPIService = services.DigitransitAPIService(db.Database(), mock_push_service.MockPushService(), 'http://localhost:11111')

    def test_get_stops(self):
        stops = self.digitransitAPIService.get_stops(60.203978, 24.9633573, 160)
        self.assertTrue("stops" in stops)

        all_stops = stops["stops"]
        self.assertEqual(len(all_stops), 1)

        stop = all_stops[0]
        self.assertTrue("stop" in stop)

        stop_data = stop["stop"]
        self.assertTrue("stop_code" in stop_data)
        self.assertTrue("stop_id" in stop_data)
        self.assertTrue("stop_name" in stop_data)
        self.assertTrue("schedule" in stop_data)

        schedule = stop_data["schedule"]
        self.assertNotEqual(len(schedule), 0)

    def test_get_stops_near_coordinates(self):
        stoplist_returns_only_three = self.digitransitAPIService.get_stops_near_coordinates(60.203978, 24.9633573, 300)
        self.assertEqual(stoplist_returns_only_three, [{'distance': 158, 'stop_id': 'HSL:1240133'}, {'distance': 196, 'stop_id': 'HSL:1240118'}, {'distance': 263, 'stop_id': 'HSL:1240103'}])

        stoplist_return_one = self.digitransitAPIService.get_stops_near_coordinates(60.203978, 24.9633573, 160)
        self.assertEqual(stoplist_return_one, [{'stop_id': 'HSL:1240133', 'distance': 158}])

        stoplist_return_none = self.digitransitAPIService.get_stops_near_coordinates(60.203978, 24.9633573, 10)
        self.assertEqual(stoplist_return_none, [])

    def test_get_busses_by_stop_id(self):
        stop = self.digitransitAPIService.get_busses_by_stop_id("HSL:1362141", 100)
        self.assertTrue("stop_name" in stop)
        self.assertEqual(stop["stop_name"], 'Viikki')
        self.assertTrue("distance" in stop)
        self.assertEqual(stop["distance"], 100)

        first = stop["schedule"][0]
        self.assertTrue("line" in first)

        #stop2 = Aamuruskonkuja(HSL:6070226)
        #testing that 60 minutes time limit works
        stop2 = self.digitransitAPIService.get_busses_by_stop_id("HSL:6070226", 100)
        stop2_schedule = stop2["schedule"]
        self.assertTrue(len(stop2_schedule) > 0)

        #stop3 = Palkkatilanportti(HSL:1171403)
        # testing that no more than two vehicles from the same route appears on schedule
        stop3 = self.digitransitAPIService.get_busses_by_stop_id("HSL:1171403", 100)
        stop3_schedule = stop3["schedule"]
        self.assertTrue(len(stop3_schedule) <= 2)

    def test_get_busses_by_stop_id_with_invalid_id(self):
        stop = self.digitransitAPIService.get_busses_by_stop_id("INVALID", 100)
        self.assertEqual(stop['error'], 'Invalid stop id')

    def test_get_stops_by_trip_id(self):
        stoptimes = self.digitransitAPIService.get_stops_by_trip_id('HSL:1506_20161031_Ti_2_1155')

        self.assertTrue("stops" in stoptimes)

        all_stoptimes = stoptimes["stops"]
        
        first_stop = all_stoptimes[0]
        self.assertTrue("stop_name" in first_stop)
        self.assertTrue("stop_id" in first_stop)
        self.assertTrue("stop_code" in first_stop)
        self.assertTrue("arrives_in" in first_stop)

        self.assertEqual(first_stop["stop_name"], 'Naistenklinikka')

        second_stop = all_stoptimes[1]
        self.assertEqual(second_stop["stop_name"], 'Tukholmankatu')

    def test_get_stops_by_trip_id_with_invalid_id(self):
        stop = self.digitransitAPIService.get_stops_by_trip_id("INVALID")
        self.assertEqual(stop['error'], 'Invalid trip id')

    def test_sending_notifications(self):
        requests = {"trip_id_1": [(1,"stop_id","device_id")], "trip_id_2": [(2,"stop_id","device_id")], "trip_id_3": [(3,"stop_id","device_id")]}
        # set arrival times in mock hsl api
        result = self.digitransitAPIService.fetch_trips_and_send_push_notifications(requests)

        self.assertEqual(2, len(result))
        self.assertTrue(1 in result)
        self.assertTrue(2 in result)

    def test_sending_error_notifications(self):
        requests = {"trip_id_1": [(1, "stop_id", "device_id")], "trip_id_2": [(2, "stop_id", "device_id")], "trip_id_3": [(3, "stop_id", "device_id")]}
        # set arrival times in mock hsl api
        result = self.digitransitAPIService.fetch_trips_and_send_push_notifications(requests)

        self.assertEqual(2, len(result))
        self.assertTrue(1 in result)
        self.assertTrue(2 in result)


if __name__ == '__main__':
    unittest.main()
