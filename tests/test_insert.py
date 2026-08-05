import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from config.snowflake_connection import insert_sensor_data

sample_data = {
    "container_id": "CONT-1001",
    "temperature": 5.7,
    "humidity": 75,
    "vibration": 0.82,
    "battery": 89,
    "timestamp": "2026-08-03 21:30:00"
}

insert_sensor_data(sample_data)