-- Round the ratings to a decimal number with 2 decimals.

SELECT
	rating,
	-- Round-up the rating to an integer value
	CEILING(rating) AS round_up,
	-- Round-down the rating to an integer value
	FLOOR(rating) AS round_down,
	-- Round the rating value to one decimal
	ROUND(rating, 1) AS round_onedec,
	-- Round the rating value to two decimals
	ROUND(rating, 2) AS round_twodec
FROM ratings;