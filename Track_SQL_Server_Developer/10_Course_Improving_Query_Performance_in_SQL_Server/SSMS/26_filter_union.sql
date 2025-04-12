SELECT CityName AS NearCityName, -- City name column
	   CountryCode
FROM Cities

UNION -- Append queries

SELECT Capital AS NearCityName, -- Nation capital column
       Code2 AS CountryCode
FROM Nations;