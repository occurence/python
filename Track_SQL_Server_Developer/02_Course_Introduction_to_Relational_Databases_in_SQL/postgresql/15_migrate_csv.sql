DROP TABLE IF EXISTS cars;
-- Create a table for the cars entity type
CREATE TABLE cars (
 make varchar(64) NOT NULL,
 model varchar(64) NOT NULL,
 mpg integer NOT NULL
);

-- Print the contents of this table
SELECT *
FROM cars;

COPY cars(make, model, mpg)
FROM 'D:\STUDY\python\Track_SQL_Server_Developer\02_Course_Introduction_to_Relational_Databases_in_SQL\datasets\cars.csv'
DELIMITER ','
CSV HEADER;

-- Print the contents of this table
SELECT *
FROM cars;