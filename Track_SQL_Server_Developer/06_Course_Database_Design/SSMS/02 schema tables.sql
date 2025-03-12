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
-- Create a week dimension table
DROP TABLE IF EXISTS week_dim;
CREATE TABLE week_dim(
	week_id INTEGER PRIMARY KEY,
    week INTEGER NOT NULL,
    month VARCHAR(160) NOT NULL,
    year INTEGER NOT NULL
);

-- Create a runs fact table
DROP TABLE IF EXISTS runs_fact;

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

WITH DistinctWeeks AS (
	SELECT
	DISTINCT week, month, year,
	MONTH(CAST('1-' + month + '-' + CAST(year AS VARCHAR(4)) AS DATETIME)) AS MonthOrder
	FROM runs
)
, RowNumbers AS (
    SELECT
        ROW_NUMBER() OVER (ORDER BY MonthOrder) + 600 AS week_id,
        week,
        month,
        year,
		MonthOrder
    FROM DistinctWeeks
)
INSERT INTO week_dim (week_id, week, month, year)
SELECT week_id, week, month, year FROM RowNumbers;

SELECT * FROM week_dim;

SELECT
	duration_mins, week_id, route_dim.route_id
INTO runs_fact
FROM runs
INNER JOIN route_dim ON route_dim.route_name = runs.route_name
INNER JOIN week_dim ON CONCAT(week_dim.week, '-', week_dim.month) = CONCAT(runs.week, '-', runs.month);

SELECT * FROM runs_fact;