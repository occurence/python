-- Select country and event_year from eurovision
SELECT 
  country, 
  eventyear 
FROM 
  eurovision;

-- Amend the code to select all columns
SELECT 
  *
FROM 
  eurovision;

-- Return all columns, restricting the percent of rows returned
SELECT 
  TOP (50) PERCENT * 
FROM 
  eurovision;