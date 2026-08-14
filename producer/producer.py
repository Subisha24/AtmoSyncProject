from kafka import KafkaProducer
from sensor_generator import generate_sensor_data
import json
import time
import random

# Container IDs already present in container_routes.csv
CONTAINER_IDS = [
    "CONT-1045",
    "CONT-1211",
    "CONT-3021",
    "CONT-4102",
    "CONT-5562",
    "CONT-6754",
    "CONT-7218",
    "CONT-8435",
    "CONT-8891",
    "CONT-9931"
]

# Create Kafka Producer
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print("Connected to Kafka...")
print("Sending sensor data...\n")

while True:

    # Generate temperature, humidity, vibration, battery, timestamp
    data = generate_sensor_data()

    # Replace random container ID with a valid route container ID
    data["container_id"] = random.choice(CONTAINER_IDS)

    producer.send(
        "container_sensor_data",
        value=data
    )

    print(data)

    time.sleep(2)