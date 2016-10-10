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
        self.assertTrue("stop_name" in stop_data)
        self.assertTrue("schedule" in stop_data)

        schedule = stop_data["schedule"]
        self.assertNotEqual(len(schedule), 0)

    def test_get_stops_near_coordinates(self):
        stoplist_returns_only_three = self.digitransitAPIService.get_stops_near_coordinates(60.203978, 24.9633573, 300)
        self.assertEqual(stoplist_returns_only_three, ['HSL:1240133', 'HSL:1240118', 'HSL:1240103'])

        stoplist_return_one = self.digitransitAPIService.get_stops_near_coordinates(60.203978, 24.9633573, 160)
        self.assertEqual(stoplist_return_one, ['HSL:1240133'])

        stoplist_return_none = self.digitransitAPIService.get_stops_near_coordinates(60.203978, 24.9633573, 10)
        self.assertEqual(stoplist_return_none, [])

    def test_get_busses_by_stop_id(self):
        stop = self.digitransitAPIService.get_busses_by_stop_id("HSL:1362141")
        self.assertTrue("stop_name" in stop)
        self.assertEqual(stop["stop_name"], 'Viikki')

        first = stop["schedule"][0]
        self.assertTrue("line" in first)


if __name__ == '__main__':
    unittest.main()
