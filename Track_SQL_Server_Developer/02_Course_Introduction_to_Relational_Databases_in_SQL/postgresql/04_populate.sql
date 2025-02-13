-- Insert unique professors into the new table
INSERT INTO professors 
SELECT DISTINCT firstname, lastname, university_shortname 
FROM university_professors;

-- Doublecheck the contents of professors
SELECT * 
FROM professors;

-- Insert unique universities into the new table
INSERT INTO universities 
SELECT DISTINCT university_shortname, university, university_city 
FROM university_professors;

-- Doublecheck the contents of universities
SELECT * 
FROM universities;

-- Insert unique organizations into the new table
INSERT INTO organizations 
SELECT DISTINCT organization, organization_sector
FROM university_professors;

-- Doublecheck the contents of organizations
SELECT * 
FROM organizations;

-- Insert unique affiliations into the new table
INSERT INTO affiliations 
SELECT DISTINCT firstname, lastname, function, organization 
FROM university_professors;

-- Doublecheck the contents of affiliations
SELECT * 
FROM affiliations;

-- Delete the university_professors table
-- DROP TABLE university_professors;

-- Doublecheck the contents of college
SELECT * 
FROM university_professors;