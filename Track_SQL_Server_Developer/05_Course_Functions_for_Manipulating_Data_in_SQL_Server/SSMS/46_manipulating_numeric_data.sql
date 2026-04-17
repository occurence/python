-- Select the number of cocoa flavors the company was rated on.
-- Select the lowest, highest and the average rating that each company received.
-- Round the average rating to 1 decimal and show it as a different column.
-- Calculate the average rating received by each company and perform the following approximations:
-- a. round-up to the next integer value
-- b. round-down to the previous integer value.

SELECT 
	company, 
    -- Select the number of cocoa flavors for each company
	COUNT(*) AS flavors,
    -- Select the minimum, maximum and average rating
	MIN(rating) AS lowest_score,   
	MAX(rating) AS highest_score,   
	AVG(rating) AS avg_score,
    -- Round the average rating to 1 decimal
    ROUND(AVG(rating), 1) AS round_avg_score,
    -- Round up and then down the aveg. rating to the next integer 
    CEILING(AVG(rating)) AS round_up_avg_score,   
	FLOOR(AVG(rating)) AS round_down_avg_score
FROM ratings
GROUP BY company
ORDER BY flavors DESC;