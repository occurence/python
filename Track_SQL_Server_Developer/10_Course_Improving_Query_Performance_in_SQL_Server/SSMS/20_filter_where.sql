SELECT Country, COUNT(*) CountOfPlayers
FROM Players
-- Add the filter condition
WHERE Country
-- Fill in the missing countries
	IN ('Argentina','Brazil','Dominican Republic'
        ,'Puerto Rico')
GROUP BY Country;