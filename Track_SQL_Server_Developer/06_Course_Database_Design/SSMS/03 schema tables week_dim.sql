USE DatabaseDesign;
GO

-- Create a dimension table called route that will hold the route information.
-- Create a dimension table called week that will hold the week information.

-- Create a week dimension table
DROP TABLE IF EXISTS week_dim;
CREATE TABLE week_dim(
	week_id INTEGER PRIMARY KEY,
    week INTEGER NOT NULL,
    month VARCHAR(160) NOT NULL,
    year INTEGER NOT NULL
);

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