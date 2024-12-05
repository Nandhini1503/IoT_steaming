import requests
import json

# Load configuration
with open('../../config/weather_api_config.json') as config_file:
    config = json.load(config_file)

API_URL = config['https://api.openweathermap.org/data/2.5/weather?q=Madurai,IN&appid=483577447574f8e96a07c5f1d745e1fe']
API_KEY = config['483577447574f8e96a07c5f1d745e1fe']
LOCATION = config['Madurai,IN']

def fetch_weather_data():
    response = requests.get(f"{API_URL}?q={LOCATION}&appid={API_KEY}")
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    data = fetch_weather_data()
    if data:
        with open('../../data/raw/weather_data.json', 'w') as f:
            json.dump(data, f, indent=4)
