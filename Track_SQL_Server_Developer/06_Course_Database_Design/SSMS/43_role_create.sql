-- Create a data scientist role
CREATE ROLE data_scientist;
GO

-- Create a role for Marta
CREATE ROLE marta LOGIN;
GO

-- Create an admin role
CREATE ROLE admin WITH CREATEDB CREATEROLE;
GO