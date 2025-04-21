SELECT WorldBankRegion,
       CountryName,
       Capital -- Capital city name column
FROM Nations
WHERE Capital NOT IN
	(SELECT NearestPop -- City name column
     FROM Earthquakes);