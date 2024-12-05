import paho.mqtt.client as mqtt
import json

# Load configuration
with open('../../config/mqtt_config.json') as config_file:
    config = json.load(config_file)

BROKER = config['broker']
PORT = config['port']
TOPIC = config['topic']

def publish_data():
    client = mqtt.Client()
    client.connect(BROKER, PORT)

    with open('../../data/raw/weather_data.json') as f:
        weather_data = json.load(f)

    client.publish(TOPIC, json.dumps(weather_data))
    client.disconnect()

if __name__ == "__main__":
    publish_data()
