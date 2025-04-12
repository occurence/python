SELECT Date, Country, Place, Depth, Magnitude
FROM Earthquakes
WHERE Magnitude > 8
    AND Depth > 500
ORDER BY Depth DESC;