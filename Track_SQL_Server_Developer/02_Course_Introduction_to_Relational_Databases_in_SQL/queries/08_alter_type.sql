-- Select the university_shortname column
-- SELECT DISTINCT(university_shortname)
SELECT CAST(university_shortname AS VARCHAR) AS university_shortname
FROM professors;

-- Specify the correct fixed-length character type
ALTER TABLE professors
ALTER COLUMN university_shortname
-- TYPE CHAR(3);
CHAR(3);

SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'professors';

-- Change the type of firstname
ALTER TABLE professors
ALTER COLUMN firstname
-- TYPE VARCHAR(64);
VARCHAR(64);

SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'professors';