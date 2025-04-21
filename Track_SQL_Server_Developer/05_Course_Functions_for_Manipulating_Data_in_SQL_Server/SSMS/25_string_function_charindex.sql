-- Restrict the query to select only the voters whose first name contains the expression "dan".
SELECT 
	first_name,
	last_name,
	email 
FROM voters
-- Look for the "dan" expression in the first_name
WHERE CHARINDEX('dan', first_name) > 0;

-- Restrict the query to select the voters with "dan" in the first_name and "z" in the last_name.
SELECT 
	first_name,
	last_name,
	email 
FROM voters
-- Look for the "dan" expression in the first_name
WHERE CHARINDEX('dan', first_name) > 0 
    -- Look for last_names that contain the letter "z"
	AND CHARINDEX('z', last_name) > 0;

-- Restrict the query to select the voters with "dan" in the first_name and DO NOT have the letter "z" in the last_name.
SELECT 
	first_name,
	last_name,
	email 
FROM voters
-- Look for the "dan" expression in the first_name
WHERE CHARINDEX('dan', first_name) > 0 
    -- Look for last_names that do not contain the letter "z"
	AND CHARINDEX('z', last_name) = 0;