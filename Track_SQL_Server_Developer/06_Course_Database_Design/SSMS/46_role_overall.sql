-- Create a login at the database level
DROP USER IF EXISTS marta;
GO
CREATE USER marta FOR LOGIN marta;
GO

-- Remove Marta from the data scientist group
-- REVOKE data_scientist FROM marta;
ALTER ROLE data_scientist DROP MEMBER marta;
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


-- Create an admin role
-- CREATE ROLE admin WITH CREATEDB, CREATEROLE;
ALTER SERVER ROLE dbcreator ADD MEMBER marta; -- CREATEDB
ALTER SERVER ROLE securityadmin ADD MEMBER marta; -- CREATEROLE



CREATE ROLE admin;
GO
ALTER ROLE admin ADD MEMBER marta;
GO

-- List all database roles and members
SELECT dp1.name AS RoleName, dp2.name AS MemberName
FROM sys.database_role_members AS drm
JOIN sys.database_principals AS dp1
    ON drm.role_principal_id = dp1.principal_id
JOIN sys.database_principals AS dp2
    ON drm.member_principal_id = dp2.principal_id
ORDER BY dp1.name, dp2.name;

-- List all users in the current database
SELECT name, type_desc
FROM sys.database_principals
WHERE type IN ('S', 'U', 'G') -- SQL user, Windows user, Windows group
  AND name NOT IN ('dbo', 'guest', 'INFORMATION_SCHEMA', 'sys');

-- List all server-level roles and their members
SELECT
    r.name AS ServerRole,
    m.name AS Member
FROM sys.server_role_members rm
JOIN sys.server_principals r ON rm.role_principal_id = r.principal_id
JOIN sys.server_principals m ON rm.member_principal_id = m.principal_id
ORDER BY r.name, m.name;

-- List all logins on the server
SELECT name, type_desc, is_disabled
FROM sys.server_principals
WHERE type IN ('S', 'U', 'G') -- SQL login, Windows login, Windows group
  AND name NOT LIKE '##%'; -- skip system logins