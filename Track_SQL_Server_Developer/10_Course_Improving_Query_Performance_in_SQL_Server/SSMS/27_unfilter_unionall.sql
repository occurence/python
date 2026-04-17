SELECT CityName AS NearCityName,
	   CountryCode
FROM Cities

UNION ALL -- Append queries

SELECT Capital AS NearCityName,
       Code2 AS CountryCode  -- Country code column
FROM Nations;