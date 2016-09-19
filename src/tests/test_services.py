import unittest
import services

class TestDigitransitAPIService(unittest.TestCase):

    def setUp(self):
        self.digitransitAPIService = services.DigitransitAPIService()

    def test_get_stops(self):
        stops = self.digitransitAPIService.get_stops(60.203978, 24.9633573)
        self.assertEqual('foo', 'foo')

    def test_get_stops_near_coordinates(self):
        self.assertEqual('foo', 'foo')

    def test_get_busses_by_stop_id(self):
        return



if __name__ == '__main__':
    unittest.main()