import unittest
import services
import db


class TestDigitransitAPIService(unittest.TestCase):

    def setUp(self):
        self.digitransitAPIService = services.DigitransitAPIService(db.Database())

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

    def test_get_stops_by_trip_id(self):
        stop_list = self.digitransitAPIService.get_stops_near_coordinates(60.1880620, 24.96290)
        stoptimes = self.digitransitAPIService.get_stops_by_trip_id('HSL:1006_20161031_Ti_1_1223', 'HSL:1121436')
        self.assertTrue("stops" in stoptimes)

        all_stoptimes = stoptimes["stops"]
        if all_stoptimes:
            first_stop = all_stoptimes[0]
            self.assertTrue("stop_name" in first_stop)
            self.assertTrue("stop_id" in first_stop)
            self.assertTrue("stop_code" in first_stop)
            self.assertTrue("arrives_in" in first_stop)

            #self.assertEqual(first_stop["stop_name"], 'Korso')

            #second_stop = all_stoptimes[1]
            #self.assertEqual(second_stop["stop_name"], 'Savio')
        empty_stoptimes = self.digitransitAPIService.get_stops_by_trip_id('HSL:1006_20161031_Ti_1_1223', 'HSL:1121436')
        self.assertEqual(empty_stoptimes, {'stops': []})

if __name__ == '__main__':
    unittest.main()
