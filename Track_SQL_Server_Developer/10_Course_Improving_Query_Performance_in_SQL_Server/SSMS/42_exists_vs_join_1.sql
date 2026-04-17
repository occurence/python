-- Initial query
SELECT TeamName,
       TeamCode,
	   City
FROM Teams AS t -- Add table
WHERE EXISTS -- Operator to compare queries
      (SELECT 1 
	  FROM Earthquakes AS e -- Add table
	  WHERE t.City = e.NearestPop);

/*
SELECT * FROM Teams
WHERE City = 'San Antonio'

SELECT * FROM Earthquakes
WHERE NearestPop = 'San Antonio'
*/