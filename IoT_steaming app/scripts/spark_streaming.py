from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, max, min, window

spark = SparkSession.builder \
    .appName("WeatherStreamProcessing") \
    .getOrCreate()

# Load data from Kafka
weather_stream = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "BROKER_ADDRESS") \
    .option("subscribe", "TOPIC_NAME") \
    .load()

weather_df = weather_stream.selectExpr("CAST(value AS STRING)")

# Transformation logic: calculate averages, max, min, etc.
processed_df = weather_df.select(
    avg(col("temperature")).alias("avg_temp"),
    max(col("temperature")).alias("max_temp"),
    min(col("temperature")).alias("min_temp")
)

query = processed_df.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
