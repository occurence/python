-- Insert unique professors into the new table
INSERT INTO professors 
SELECT DISTINCT firstname, lastname, university_shortname 
-- FROM university_professors;
FROM college;

-- Doublecheck the contents of professors
SELECT * 
FROM professors;

-- Insert unique affiliations into the new table
INSERT INTO affiliations 
SELECT DISTINCT firstname, lastname, [function], organization 
-- FROM university_professors;
FROM college;

-- Doublecheck the contents of affiliations
SELECT * 
FROM affiliations;

-- Delete the university_professors table
-- DROP TABLE university_professors;
DROP TABLE college;

-- Doublecheck the contents of college
SELECT * 
FROM college;