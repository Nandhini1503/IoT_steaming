import unittest
import requests
import json

class TestWeatherAPI(unittest.TestCase):
    def setUp(self):
        with open('../config/weather_api_config.json') as f:
            self.config = json.load(f)
    
    def test_fetch_weather(self):
        response = requests.get(f"{self.config['api_url']}?q={self.config['location']}&appid={self.config['api_key']}")
        self.assertEqual(response.status_code, 200)
        self.assertIn("weather", response.json())

if __name__ == '__main__':
    unittest.main()
