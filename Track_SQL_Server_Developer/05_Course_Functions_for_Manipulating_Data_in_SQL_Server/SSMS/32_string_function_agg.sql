-- Create a list with all the values found in the bean_origin column for the companies: 'Bar Au Chocolat', 'Chocolate Con Amor', 'East Van Roasters'. The values should be separated by commas (,).

SELECT
	-- Create a list with all bean origins, delimited by comma
	STRING_AGG(bean_origin, ',') AS bean_origins
FROM ratings
WHERE company IN ('Bar Au Chocolat', 'Chocolate Con Amor', 'East Van Roasters');