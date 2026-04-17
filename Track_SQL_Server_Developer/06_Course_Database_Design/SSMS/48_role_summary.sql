-- Create Login (Server-Level)
CREATE LOGIN [LoginName] WITH PASSWORD = 'StrongPassword';

-- Create User (Database-Level)
CREATE USER [UserName] FOR LOGIN [LoginName];

-- Create Server Role (Group at Server-Level)
CREATE SERVER ROLE [ServerRoleName];
ALTER SERVER ROLE [ServerRoleName] ADD MEMBER [LoginName];

-- Create Database Role (Group at Database-Level)
CREATE ROLE [DbRoleName];
ALTER ROLE [DbRoleName] ADD MEMBER [UserName];

-- View Server Logins and Roles
SELECT * FROM sys.server_principals;         -- All server-level logins and roles
SELECT * FROM sys.server_role_members;       -- Membership of server roles

-- View Database Users and Roles
SELECT * FROM sys.database_principals;       -- All users and roles in the database
SELECT * FROM sys.database_role_members;     -- Membership of database roles

-- Add Member to Server Role
ALTER SERVER ROLE [ServerRoleName] ADD MEMBER [LoginName];

-- Remove Member from Server Role
ALTER SERVER ROLE [ServerRoleName] DROP MEMBER [LoginName];

-- Add Member to Database Role
ALTER ROLE [DbRoleName] ADD MEMBER [UserName];

-- Remove Member from Database Role
ALTER ROLE [DbRoleName] DROP MEMBER [UserName];

-- Change Login Password
ALTER LOGIN [LoginName] WITH PASSWORD = 'NewStrongPassword';

-- Drop Database User
DROP USER [UserName];

-- Drop Login
DROP LOGIN [LoginName];

-- Drop Server Role (if no members)
DROP SERVER ROLE [ServerRoleName];

-- Drop Database Role
DROP ROLE [DbRoleName];