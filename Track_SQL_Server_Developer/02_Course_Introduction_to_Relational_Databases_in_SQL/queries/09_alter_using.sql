-- Convert the values in firstname to a max. of 16 characters
ALTER TABLE professors 
ALTER COLUMN firstname 
-- TYPE varchar(16)
-- USING SUBSTRING(firstname, 1, 16)
VARCHAR(16)
USING SUBSTRING(firstname, 1, 16)