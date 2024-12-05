import unittest
from kafka import KafkaProducer

class TestKafkaProducer(unittest.TestCase):
    def test_kafka_connection(self):
        producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
        self.assertIsNotNone(producer)

if __name__ == '__main__':
    unittest.main()
