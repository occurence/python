SELECT * 
FROM Nations
WHERE CountryName LIKE 'U%'
SELECT *
FROM Players
WHERE Country LIKE 'U%'

/*
SELECT 'Nations' AS TableName, CountryName 
FROM Nations -- Table from Earthquakes database
WHERE Code2 = 'US'

UNION ALL -- Operator for the intersect between tables

SELECT 'Players' AS TableName, Country
FROM Players
WHERE Country = 'USA'; -- Table from NBA Season 2017-2018 database
*/