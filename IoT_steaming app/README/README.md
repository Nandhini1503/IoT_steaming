# IoT Streaming Application for Weather Data

## Overview
This project streams weather data from an external API, processes it using Apache Spark, and displays the results on a live dashboard.

## Architecture
- **Weather API:** Fetches real-time weather data.
- **MQTT Broker:** Publishes data in real-time.
- **Kafka:** Serves as a message queue for streaming data.
- **Apache Spark:** Processes and calculates insights from the streaming data.
- **MongoDB:** Stores the processed data.
- **Flask Dashboard:** Displays live weather data on a web interface.

## Features
- Hourly and daily weather data analysis.
- Real-time dashboard visualization.
- Alerts for extreme weather conditions (future feature).

## Prerequisites
- Python 3.8+
- Apache Kafka and Zookeeper
- MongoDB
- Flask
- Apache Spark with PySpark

## Setup Instructions

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-repo/iot-streaming-app.git
    cd iot-streaming-app
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Start services:**
    - Start Kafka and Zookeeper:
        ```bash
        zookeeper-server-start.sh config/zookeeper.properties
        kafka-server-start.sh config/server.properties
        ```
    - Start MongoDB:
        ```bash
        mongod --dbpath /data/db
        ```

4. **Run the scripts in the following order:**
    - Fetch weather data: `python scripts/weather_api/fetch_weather.py`
    - Publish to MQTT: `python scripts/mqtt_broker/publish_weather.py`
    - Kafka Producer: `python scripts/kafka/kafka_producer.py`
    - Spark Processing: `spark-submit scripts/spark_streaming/process_stream.py`

5. **Run the Dashboard:**
    ```bash
    cd dashboard/live_dashboard
    python app.py
    ```

6. **Access the Dashboard:**
    - Open your browser and go to: `http://127.0.0.1:5000/`

---

## Contributions
Feel free to fork and contribute to this project!

## License
MIT License.
