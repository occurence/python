-- Create an alias for each voter with the following parts: the first 3 letters from the first name concatenated with the last 3 letters from the last name, followed by the _ character and the last 2 digits from the birth date.
SELECT 
	first_name,
	last_name,
	country,
    -- Select only the first 3 characters from the first name
	LEFT(first_name, 3) AS part1,
    -- Select only the last 3 characters from the last name
    RIGHT(last_name, 3) AS part2,
    -- Select only the last 2 digits from the birth date
    RIGHT(birthdate, 2) AS part3,
    -- Create the alias for each voter
    LEFT(first_name, 3) + RIGHT(last_name, 3) + '_' + RIGHT(birthdate, 2) 
FROM voters;