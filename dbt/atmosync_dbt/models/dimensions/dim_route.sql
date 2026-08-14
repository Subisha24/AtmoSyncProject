{{ config(materialized='table') }}

SELECT
    container_id,
    commodity,
    source_city,
    destination_city,
    distance_km,
    estimated_travel_hours
FROM {{ ref('container_routes') }}