/*
Location of the epicenter of earthquakes with a 9+ magnitude
*/

-- Replace City with the correct column name
SELECT n.CountryName AS Country
	,e.NearestPop AS ClosestCity
    ,e.Date
    ,e.Magnitude
FROM Nations AS n
INNER JOIN Earthquakes AS e
	ON n.Code2 = e.Country
WHERE e.Magnitude >= 9
ORDER BY e.Magnitude DESC;