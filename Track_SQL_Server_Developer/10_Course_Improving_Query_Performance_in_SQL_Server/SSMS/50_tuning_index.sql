-- Query 1
SELECT *
FROM Cities
WHERE CountryCode = 'RU' -- Country code
		OR CountryCode = 'CN' -- Country code

-- Query 2
SELECT *
FROM Cities
WHERE CountryCode IN ('JM', 'NZ') -- Country codes

/*
4694 results returned
Table 'Cities'. ..., logical reads 274, ... ,

212 results returned
Table 'Cities'. ..., logical reads 10, ... ,
*/