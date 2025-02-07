-- Retrieve the minimum and maximum place, and point values
SELECT 
  -- the lower the value the higher the place, so MIN = the highest placing
  MIN(place) AS hi_place, 
  MAX(place) AS lo_place, 
  -- Retrieve the minimum and maximum points values. This time MIN = the lowest points value
  MIN(points) AS min_points, 
  MAX(points) AS max_points 
FROM 
  eurovision;

-- Retrieve the minimum and maximum place, and point values
SELECT 
  -- the lower the value the higher the place, so MIN = the highest placing
  MIN(place) AS hi_place, 
  MAX(place) AS lo_place,  
  -- Retrieve the minimum and maximum points values. This time MIN = the lowest points value
  MIN(points) AS min_points, 
  MAX(points) AS max_points 
FROM 
  eurovision
  -- Group by country
GROUP BY
  country;

-- Obtain a count for each country
SELECT 
  COUNT(country) AS country_count, 
  -- Retrieve the country column
  country, 
  -- Return the average of the Place column 
  -- AVG(place) AS average_place, 
  AVG(CAST(place AS FLOAT)) AS average_place, 
  -- AVG(points) AS avg_points, 
  AVG(CAST(points AS FLOAT)) AS avg_points, 
  MIN(points) AS min_points, 
  MAX(points) AS max_points 
FROM 
  eurovision 
GROUP BY 
  country;

SELECT 
  country, 
  COUNT (country) AS country_count, 
  -- AVG (place) AS avg_place, 
  AVG (place) AS avg_place, 
  AVG (points) AS avg_points, 
  MIN (points) AS min_points, 
  MAX (points) AS max_points 
FROM 
  eurovision 
GROUP BY 
  country 
  -- The country column should only contain those with a count greater than 5
HAVING 
  COUNT(country) > 5 
  -- Arrange columns in the correct order
ORDER BY 
  avg_place, 
  avg_points DESC;