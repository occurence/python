-- Select only the voters whose first name has fewer than 5 characters and email address meets these conditions in the same time: (1) starts with the letter “j”, (2) the third letter is “a” and (3) is created at yahoo.com.
-- Concatenate the first name and last name in the same column and present it in this format: " *** Firstname LASTNAME *** ".
-- Mask the year part from the birthdate column, by replacing the last two digits with "XX" (1986-03-26 becomes 19XX-03-26).

SELECT
    -- Concatenate the first and last name
	CONCAT('***' , first_name, ' ', UPPER(last_name), '***') AS name,
    -- Mask the last two digits of the year
    REPLACE(birthdate, SUBSTRING(CAST(birthdate AS varchar), 3, 2), 'XX') AS birthdate,
	email,
	country
FROM voters
   -- Select only voters with a first name less than 5 characters
WHERE LEN(first_name) < 5
   -- Look for this pattern in the email address: "j%[0-9]@yahoo.com"
	AND PATINDEX('j_a%@yahoo.com', email) > 0;    