-- Write a query to select the voters whose first name contains the letters "rr".
SELECT 
	first_name,
	last_name,
	email 
FROM voters
-- Look for first names that contain "rr" in the middle
WHERE PATINDEX('%rr%', first_name) > 0;

-- Write a query to select the voters whose first name starts with "C" and has "r" as the third letter.
SELECT 
	first_name,
	last_name,
	email 
FROM voters
-- Look for first names that start with C and the 3rd letter is r
WHERE PATINDEX('C_r%', first_name) > 0;

-- Select the voters whose first name contains an "a" followed by other letters, then a "w", followed by other letters.
SELECT 
	first_name,
	last_name,
	email 
FROM voters
-- Look for first names that have an "a" followed by 0 or more letters and then have a "w"
WHERE PATINDEX('%a%w%', first_name) > 0;

-- Write a query to select the voters whose first name contains one of these letters: "x", "w" or "q".
SELECT 
	first_name,
	last_name,
	email 
FROM voters
-- Look for first names that contain one of the letters: "x", "w", "q"
WHERE PATINDEX('%[xwq]%', first_name) > 0;