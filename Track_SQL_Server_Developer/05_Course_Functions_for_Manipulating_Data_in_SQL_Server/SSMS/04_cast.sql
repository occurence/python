SELECT 
	-- Transform the year part from the birthdate to a string
	first_name + ' ' + last_name + ' was born in ' + CAST(YEAR(birthdate) AS nvarchar) + '.' 
FROM voters;

SELECT 
	-- Transform to int the division of total_votes to 5.5
	CAST(total_votes/5.5 AS INT) AS DividedVotes
FROM voters;

SELECT 
	first_name,
	last_name,
	total_votes
FROM voters
-- Transform the total_votes to char of length 10
WHERE CAST(total_votes AS CHAR(10)) LIKE '5%';