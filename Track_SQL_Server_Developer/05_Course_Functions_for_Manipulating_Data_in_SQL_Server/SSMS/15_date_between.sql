-- Calculate the number of years since a participant celebrated their 18th birthday until the first time they voted.
SELECT
	first_name,
	birthdate,
	first_vote_date,
    -- Select the diff between the 18th birthday and first vote
	DATEDIFF(YEAR, DATEADD(YEAR, 18, birthdate), first_vote_date) AS adult_years_until_vote
FROM voters;

-- How many weeks have passed since the beginning of 2019 until now?
SELECT 
	-- Get the difference in weeks from 2019-01-01 until now
	DATEDIFF(WEEK, '2019-01-01', GETDATE()) AS weeks_passed;