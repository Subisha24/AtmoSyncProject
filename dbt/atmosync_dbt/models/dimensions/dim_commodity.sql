{{ config(materialized='table') }}

SELECT
    commodity,
    category,
    price_per_kg,
    ideal_min_temp,
    ideal_max_temp,
    shelf_life_days
FROM {{ ref('commodity_pricing') }}