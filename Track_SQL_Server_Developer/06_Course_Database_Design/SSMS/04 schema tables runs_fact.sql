USE DatabaseDesign;
GO

-- Create a dimension table called route that will hold the route information.
-- Create a dimension table called week that will hold the week information.

-- Create a runs fact table
DROP TABLE IF EXISTS runs_fact;

SELECT
	duration_mins, week_id, route_dim.route_id
INTO runs_fact
FROM runs
INNER JOIN route_dim ON route_dim.route_name = runs.route_name
INNER JOIN week_dim ON CONCAT(week_dim.week, '-', week_dim.month) = CONCAT(runs.week, '-', runs.month);

SELECT * FROM runs_fact;