import unittest
import sys
#from src.stop import app


class TestStopRoutes(unittest.TestCase):

  #  def setUp(self):
#      app.config['TESTING'] = True
  #      self.app = app.test_client()

    def test_hello(self):
        self.assertEqual('foo', 'foo')

    # def test_stops_get(self):
    #     response = self.app.get('/stops?lat=1.0&lon=2.0')
    #     self.assertEquals(response.status_code, 200)

if __name__ == '__main__':
    print(sys.path)
    unittest.main()
