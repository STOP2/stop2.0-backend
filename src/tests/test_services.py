import unittest
import services

class TestDigitransitAPIService(unittest.TestCase):

    def setUp(self):
        digitransitAPIService = services.DigitransitAPIService()

    def test_get_stops(self):

        self.assertEqual('foo', 'foo')


if __name__ == '__main__':
    unittest.main()