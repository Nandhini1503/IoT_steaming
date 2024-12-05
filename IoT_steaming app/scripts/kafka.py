from kafka import KafkaProducer
import json

# Load configuration
with open('../../config/kafka_config.json') as config_file:
    config = json.load(config_file)

TOPIC = config['topic']
BROKER = config['broker']

producer = KafkaProducer(bootstrap_servers=9092, value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def send_to_kafka(data):
    producer.send(TOPIC, data)
    sample_data = {'temperature': 32, 'humidity': 58}
publish_to_kafka(sample_data)

if __name__ == "__main__":
    with open('../../data/raw/weather_data.json') as f:
        weather_data = json.load(f)
        send_to_kafka(weather_data)
