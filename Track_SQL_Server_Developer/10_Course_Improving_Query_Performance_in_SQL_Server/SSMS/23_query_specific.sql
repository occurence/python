SELECT latitude, -- Y location coordinate column
       longitude, -- X location coordinate column
	   magnitude , -- Earthquake strength column
	   depth, -- Earthquake depth column
	   NearestPop -- Nearest city column
FROM Earthquakes
WHERE Country = 'PG' -- Papua New Guinea country code
	OR Country = 'ID'; -- Indonesia country code