-- Select the first 20 rows from the specified columns
SELECT 
  TOP (20) description, 
  event_date 
FROM 
  grid 
  -- Order your results by the event_date column
ORDER BY event_date;

-- Select the top 20 rows from description, nerc_region and event_date
SELECT 
  TOP (20) description,
  nerc_region,
  event_date
FROM 
  grid 
  -- Order by nerc_region, affected_customers & event_date
  -- event_date should be in descending order
ORDER BY
  nerc_region,
  affected_customers,
  event_date DESC;