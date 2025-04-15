-- SELECT the country column FROM the eurovision table
SELECT
  country
FROM
  eurovision;

-- Limit the number of rows returned
SELECT 
  TOP (50) country 
FROM 
  eurovision;

-- Return unique countries and use an alias
SELECT 
  DISTINCT country AS unique_country 
FROM 
  eurovision;