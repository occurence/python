-- Arrange the values from the list in alphabetical order.

SELECT 
	company,
    -- Create a list with all bean origins ordered alphabetically
	STRING_AGG(bean_origin, ',') WITHIN GROUP (ORDER BY bean_origin) AS bean_origins
FROM ratings
WHERE company IN ('Bar Au Chocolat', 'Chocolate Con Amor', 'East Van Roasters')
-- Specify the columns used for grouping your data
GROUP BY company;