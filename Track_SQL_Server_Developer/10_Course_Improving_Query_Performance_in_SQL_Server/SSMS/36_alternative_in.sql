-- First attempt
SELECT CountryName,
       Pop2017, -- 2017 country population
	   Capital, -- Capital city	   
       WorldBankRegion
FROM Nations
WHERE Capital IN -- Add the operator to compare queries
        (SELECT NearestPop 
	     FROM Earthquakes);