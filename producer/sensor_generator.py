import random
from datetime import datetime
from faker import Faker

fake = Faker()

def generate_sensor_data():
    data = {
        "container_id": fake.bothify(text="CONT-####"),
        "temperature": round(random.uniform(2.0, 8.0), 2),
        "humidity": random.randint(50, 90),
        "vibration": round(random.uniform(0.1, 2.5), 2),
        "battery": random.randint(40, 100),
        "timestamp": datetime.now().isoformat()
    }

    return data


if __name__ == "__main__":
    print(generate_sensor_data())