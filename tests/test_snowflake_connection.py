import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config.snowflake_connection import get_connection

from config.snowflake_connection import get_connection

try:
    conn = get_connection()
    print("✅ Successfully connected to Snowflake!")

    conn.close()

except Exception as e:
    print("❌ Connection failed!")
    print(e)