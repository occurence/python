SELECT Code2 -- Add the country code column
FROM Nations

EXCEPT -- Add the operator to compare the two queries

SELECT Country 
FROM Earthquakes; -- Table with country codes

/*
SELECT 'Nations' AS TableName, Code2
FROM Nations
WHERE Code2 = 'HK'

UNION ALL

SELECT 'Earthquakes' AS TableName, Country
FROM Earthquakes
WHERE Country = 'HK'
*/