-- Retrieve the date when each voter had their 18th birthday.
SELECT 
	first_name,
	birthdate,
    -- Add 18 years to the birthdate
	DATEADD(YEAR, 18, birthdate) AS eighteenth_birthday
  FROM voters;

-- Add five days to the first_vote_date, to calculate the date when the vote was processed.
SELECT 
	first_name,
	first_vote_date,
    -- Add 5 days to the first voting date
	DATEADD(DAY, 5, first_vote_date) AS processing_vote_date
  FROM voters;

-- Calculate what day it was 476 days ago.
SELECT
	-- Subtract 476 days from the current date
	DATEADD(DAY, -476, GETDATE()) AS date_476days_ago;