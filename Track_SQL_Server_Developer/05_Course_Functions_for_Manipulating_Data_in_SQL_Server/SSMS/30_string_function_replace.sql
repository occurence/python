-- Add a new column in the query in which you replace the "yahoo.com" in all email addresses with "live.com".
SELECT 
	first_name,
	last_name,
	email,
	-- Replace "yahoo.com" with "live.com"
	REPLACE(email, 'yahoo.com', 'live.com') AS new_email
FROM voters;

-- Replace the character "&" from the company name with "and".
SELECT 
	company AS initial_name,
    -- Replace '&' with 'and'
	REPLACE(company, '&', 'and') AS new_name 
FROM ratings
WHERE CHARINDEX('&', company) > 0;

-- Remove the string "(Valrhona)" from the company name "La Maison du Chocolat (Valrhona)".
SELECT 
	company AS old_company,
    -- Remove the text '(Valrhona)' from the name
	REPLACE(company, '(Valrhona)', '') AS new_company,
	bean_type,
	broad_bean_origin
FROM ratings
WHERE company = 'La Maison du Chocolat (Valrhona)';