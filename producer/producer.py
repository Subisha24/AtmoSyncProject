from kafka import KafkaProducer
from sensor_generator import generate_sensor_data
import json
import time

# Create Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("Connected to Kafka...")
print("Sending sensor data...\n")

while True:
    data = generate_sensor_data()

    producer.send(
        "container_sensor_data",
        value=data
    )

    print(data)

    time.sleep(2)