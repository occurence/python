SELECT Team, 
    SUM(TotalPoints) AS TotalCPoints
FROM PlayerStats
WHERE Position = 'C'
GROUP BY Team
HAVING SUM(TotalPoints) > 2500;