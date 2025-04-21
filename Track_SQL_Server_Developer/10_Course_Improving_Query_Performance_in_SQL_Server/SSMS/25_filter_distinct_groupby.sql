SELECT NearestPop, 
       Country, 
       COUNT(NearestPop) NumEarthquakes -- Number of cities
FROM Earthquakes
WHERE Magnitude >= 8
	AND Country IS NOT NULL
GROUP BY Country, NearestPop -- Group columns
ORDER BY NumEarthquakes DESC;

SELECT DISTINCT(NearestPop),-- Remove duplicate city
		Country
FROM Earthquakes
WHERE MAGNITUDE >= 8 -- Add filter condition 
	AND NearestPop IS NOT NULL
ORDER BY NearestPop;

SELECT NearestPop, 
       Country, 
       COUNT(NearestPop) NumEarthquakes -- Number of cities
FROM Earthquakes
WHERE Magnitude >= 8
	AND Country IS NOT NULL
GROUP BY Country, NearestPop -- Group columns
ORDER BY NumEarthquakes DESC;