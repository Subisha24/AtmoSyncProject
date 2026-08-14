{{ config(materialized='view') }}

SELECT
    CONTAINER_ID,
    TEMPERATURE,
    HUMIDITY,
    VIBRATION,
    BATTERY,
    EVENT_TIME
FROM {{ source('raw', 'RAW_SENSOR_DATA') }}
WHERE TEMPERATURE IS NOT NULL