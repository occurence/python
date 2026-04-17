/*
select PlayerName, Country,
round(Weight_kg/SQUARE(Height_cm/100),2) BMI
from Players Where Country = 'USA'
Or Country = 'Canada'
order by BMI;
*/

SELECT PlayerName, Country,
    ROUND(Weight_kg/SQUARE(Height_cm/100),2) AS BMI
FROM Players
WHERE Country = 'USA'
    OR Country = 'Canada'
ORDER BY BMI;