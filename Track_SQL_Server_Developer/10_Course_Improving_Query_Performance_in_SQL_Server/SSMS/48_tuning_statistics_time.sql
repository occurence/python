SET STATISTICS TIME ON -- Turn the time command on

-- Query 1
SELECT * 
FROM Teams
-- Sub-query 1
WHERE City IN -- Sub-query filter operator
      (SELECT CityName 
       FROM Cities) -- Table from Earthquakes database
-- Sub-query 2
   AND City IN -- Sub-query filter operator
	   (SELECT CityName 
	    FROM Cities
		WHERE CountryCode IN ('US','CA'))
-- Sub-query 3
    AND City IN -- Sub-query filter operator
        (SELECT CityName 
         FROM Cities
	     WHERE Pop2017 >2000000);

-- Query 2
SELECT * 
FROM Teams AS t
WHERE EXISTS -- Sub-query filter operator
	(SELECT 1 
     FROM Cities AS c
     WHERE t.City = c.CityName -- Columns being compared
        AND c.CountryCode IN ('US','CA')
          AND c.Pop2017 > 2000000);

SET STATISTICS TIME OFF -- Turn the time command off

/*
 SQL Server Execution Times:
   CPU time = 15 ms,  elapsed time = 23 ms.

 SQL Server Execution Times:
   CPU time = 0 ms,  elapsed time = 4 ms.
   */