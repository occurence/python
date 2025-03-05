SELECT 
	email,
    -- Convert birthdate to varchar show it like: "Mon dd,yyyy" 
    CONVERT(varchar, birthdate, 107) AS birthdate
FROM voters;

SELECT 
	company,
    bean_origin,
    -- Convert the rating column to an integer
    CONVERT(INT, rating) AS rating
FROM ratings;

SELECT 
	company,
    bean_origin,
    rating
FROM ratings
-- Convert the rating to an integer before comparison
WHERE CONVERT(INT, rating) = 3;