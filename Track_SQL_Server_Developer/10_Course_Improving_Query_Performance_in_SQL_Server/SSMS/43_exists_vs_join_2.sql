-- Second query
SELECT t.TeamName,
       t.TeamCode,
	   t.City,
	   e.Date,
	   e.Place, -- Place description
	   e.Country -- Country code
FROM Teams AS t
INNER JOIN Earthquakes AS e -- Operator to compare tables
	  ON t.City = e.NearestPop

/*
SELECT * FROM Teams
WHERE City = 'San Antonio'

SELECT * FROM Earthquakes
WHERE NearestPop = 'San Antonio'
*/