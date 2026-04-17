-- Count the number of voters for each group.
-- Calculate the total number of votes per group.

SELECT 
	gender, 
	-- Count the number of voters for each group
	COUNT(total_votes) AS voters,
	-- Calculate the total number of votes per group
	SUM(total_votes) AS total_votes
FROM voters
GROUP BY gender;