-- Create a list with the values found in the bean_origin column for each of the companies: 'Bar Au Chocolat', 'Chocolate Con Amor', 'East Van Roasters'. The values should be separated by commas (,).

SELECT 
	company,
    -- Create a list with all bean origins
	STRING_AGG(bean_origin, ',') AS bean_origins
FROM ratings
WHERE company IN ('Bar Au Chocolat', 'Chocolate Con Amor', 'East Van Roasters')
-- Specify the columns used for grouping your data
GROUP BY company;