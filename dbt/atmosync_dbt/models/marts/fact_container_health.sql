{{ config(materialized='table') }}

SELECT
    s.container_id,
    r.commodity,
    r.source_city,
    r.destination_city,
    r.distance_km,
    r.estimated_travel_hours,

    c.category,
    c.price_per_kg,
    c.ideal_min_temp,
    c.ideal_max_temp,
    c.shelf_life_days,

    s.temperature,
    s.humidity,
    s.vibration,
    s.battery,
    s.event_time

FROM {{ ref('stg_sensor_data') }} s

LEFT JOIN {{ ref('dim_route') }} r
ON s.container_id = r.container_id

LEFT JOIN {{ ref('dim_commodity') }} c
ON r.commodity = c.commodity