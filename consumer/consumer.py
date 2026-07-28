from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "container_sensor_data",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="latest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("Listening for sensor data...\n")

for message in consumer:
    print(message.value) 