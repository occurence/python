SELECT Country, COUNT(*) CountOfPlayers 
FROM Players
GROUP BY Country
HAVING Country 
    IN ('Argentina','Brazil','Dominican Republic'
        ,'Puerto Rico');