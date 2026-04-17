-- Add the university_shortname column
ALTER TABLE professors
-- ADD COLUMN university_shortname text;
ADD university_shortname text;

-- Print the contents of this table
SELECT * 
FROM professors;

-- ALTER TABLE affiliations
-- RENAME COLUMN organisation TO organization
EXEC sp_rename 'affiliations.organisation', 'organization', 'COLUMN';

-- Delete the university_shortname column
ALTER TABLE affiliations
DROP COLUMN university_shortname;

-- Print the contents of this table
SELECT *
FROM affiliations;