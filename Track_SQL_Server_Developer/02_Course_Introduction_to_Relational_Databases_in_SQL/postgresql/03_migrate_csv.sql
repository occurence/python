DROP TABLE IF EXISTS university_professors;
-- Create a table for the university_professors entity type
CREATE TABLE university_professors(
  firstname text,
  lastname text,
  university text,
  university_shortname text,
  university_city text,
  function text,
  organization text,
  organization_sector text
);

-- Print the contents of this table
SELECT *
FROM university_professors;

COPY university_professors(firstname, lastname, university, university_shortname, university_city, function, organization, organization_sector)
FROM 'D:\STUDY\python\Track_SQL_Server_Developer\02_Course_Introduction_to_Relational_Databases_in_SQL\datasets\university_professors.csv'
DELIMITER ','
CSV HEADER;

-- Print the contents of this table
SELECT *
FROM university_professors;