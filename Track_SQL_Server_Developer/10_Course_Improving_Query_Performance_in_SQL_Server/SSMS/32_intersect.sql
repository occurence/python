SELECT Capital
FROM Nations -- Table with capital cities

INTERSECT -- Add the operator to compare the two queries

SELECT NearestPop -- Add the city name column
FROM Earthquakes;

/*
SELECT 'Nations' AS TableName, Capital
FROM Nations
WHERE Capital = 'Suva'

UNION ALL

SELECT 'Earthquakes' AS TableName, NearestPop
FROM Earthquakes
WHERE NearestPop = 'Suva'
*/