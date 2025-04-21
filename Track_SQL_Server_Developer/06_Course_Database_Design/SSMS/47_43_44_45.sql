-- Remove Marta from the data scientist group
-- REVOKE data_scientist FROM marta;
ALTER ROLE data_scientist DROP MEMBER marta;
GO

-- Create a login at the database level
DROP USER IF EXISTS marta;
GO
CREATE USER marta FOR LOGIN marta;
GO

-- Create a data scientist role
DROP ROLE IF EXISTS data_scientist;
GO
CREATE ROLE data_scientist;
GO

-- Add Marta to the data scientist group
-- GRANT data_scientist TO marta;
ALTER ROLE data_scientist ADD MEMBER marta;
GO

-- Create a login at the server level auth
DROP LOGIN marta;
GO
CREATE LOGIN marta WITH PASSWORD = 'StrongPasswordHere!';
GO

-- Create an admin role
-- CREATE ROLE admin WITH CREATEDB CREATEROLE;
-- Step 1: Create a login to represent the "admin"
DROP LOGIN admin;
GO
CREATE LOGIN admin WITH PASSWORD = 'StrongPasswordHere!';
GO

-- Step 2: Grant server-level privileges
ALTER SERVER ROLE dbcreator ADD MEMBER admin;      -- same as CREATEDB
ALTER SERVER ROLE securityadmin ADD MEMBER admin;  -- same as CREATEROLE
GO

-- Grant data_scientist update and insert privileges
GRANT UPDATE, INSERT ON long_reviews TO data_scientist;