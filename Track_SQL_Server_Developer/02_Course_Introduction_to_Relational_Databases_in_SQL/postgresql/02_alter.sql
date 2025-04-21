-- Add the university_shortname column
ALTER TABLE professors
ADD COLUMN university_shortname text;

-- Print the contents of this table
SELECT * 
FROM professors;

-- Print the contents of this table
SELECT *
FROM affiliations;

ALTER TABLE affiliations
RENAME COLUMN organisation TO organization;

-- Print the contents of this table
SELECT *
FROM affiliations;

-- Delete the university_shortname column
ALTER TABLE affiliations
DROP COLUMN university_shortname;

-- Print the contents of this table
SELECT *
FROM affiliations;