DROP TABLE IF EXISTS professors;
-- Create a table for the professors entity type
CREATE TABLE professors(
 firstname text,
 lastname text
);


-- Print the contents of this table
SELECT * 
FROM professors;

DROP TABLE IF EXISTS universities;
-- Create a table for the universities entity type
CREATE TABLE universities(
  university_shortname text,
  university text,
  university_city text
);

-- Print the contents of this table
SELECT * 
FROM universities;

DROP TABLE IF EXISTS organizations;
-- Create a table for the organizations entity type
CREATE TABLE organizations(
  organization text,
  organization_sector text
);

-- Print the contents of this table
SELECT * 
FROM organizations;

DROP TABLE IF EXISTS affiliations;
-- Create a table for the affiliations entity type
CREATE TABLE affiliations(
  firstname text,
  lastname text,
  university_shortname text,
  function text,
  organisation text
);

-- Print the contents of this table
SELECT *
FROM affiliations;