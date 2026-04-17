USE DatabaseDesign;
GO

-- Create a dimension table called route that will hold the route information.
-- Create a dimension table called week that will hold the week information.

-- Create a route dimension table
DROP TABLE IF EXISTS route_dim;
CREATE TABLE route_dim(
	route_id INTEGER PRIMARY KEY,
    park_name VARCHAR(160) NOT NULL,
    city_name VARCHAR(160) NOT NULL,
    distance_km FLOAT NOT NULL,
    route_name VARCHAR(160) NOT NULL
);


WITH DistinctRuns AS (
    SELECT DISTINCT
        park_name,
        city_name,
        distance_km,
        route_name
    FROM RUNS
)
, RowNumbers AS (
    SELECT
        ROW_NUMBER() OVER (ORDER BY CASE WHEN city_name = 'Jersey City' THEN 1 ELSE 0 END, city_name, park_name) + 100 AS route_id,
        park_name,
        city_name,
        distance_km,
        route_name
    FROM DistinctRuns
)
INSERT INTO route_dim (route_id, park_name, city_name, distance_km, route_name)
SELECT
    route_id,
    park_name,
    city_name,
    distance_km,
    route_name
FROM RowNumbers;

SELECT * FROM route_dim;