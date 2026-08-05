import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from kafka import KafkaConsumer
import json

from config.snowflake_connection import insert_sensor_data

print("🚀 Starting Kafka Consumer...")

consumer = KafkaConsumer(
    "container_sensor_data",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="latest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("✅ Connected to Kafka")
print("📡 Listening for sensor data...\n")

for message in consumer:
    sensor_data = message.value

    print(f"📦 Received: {sensor_data}")

    try:
        insert_sensor_data(sensor_data)
        print("✅ Data inserted into Snowflake\n")

    except Exception as e:
        print(f"❌ Error: {e}")