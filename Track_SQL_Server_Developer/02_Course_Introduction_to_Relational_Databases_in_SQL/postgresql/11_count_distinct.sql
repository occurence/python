-- Count the number of rows in universities
SELECT COUNT(DISTINCT(university)) 
FROM universities;

-- Count the number of distinct values in the university_city column
SELECT COUNT(DISTINCT(university_city)) 
FROM universities;