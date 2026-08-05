import os
from dotenv import load_dotenv
import snowflake.connector

load_dotenv()


def get_connection():
    return snowflake.connector.connect(
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA")
    )


def insert_sensor_data(sensor_data):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = """
        INSERT INTO RAW_SENSOR_DATA
        (
            CONTAINER_ID,
            TEMPERATURE,
            HUMIDITY,
            VIBRATION,
            BATTERY,
            EVENT_TIME
        )
        VALUES (%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(
            query,
            (
                sensor_data["container_id"],
                sensor_data["temperature"],
                sensor_data["humidity"],
                sensor_data["vibration"],
                sensor_data["battery"],
                sensor_data["timestamp"],
            ),
        )

        conn.commit()

        print("✅ Row inserted into Snowflake")

    except Exception as e:
        print("❌ Error inserting row")
        print(e)

    finally:
        cursor.close()
        conn.close()