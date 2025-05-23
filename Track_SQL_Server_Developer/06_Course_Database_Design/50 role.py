import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=DatabaseDesign;" "Trusted_Connection=True;" )
cursor = conn.cursor()

cursor.execute("""
-- Login (Server-Level)
DROP LOGIN LoginName;
CREATE LOGIN LoginName WITH PASSWORD = 'StrongPassword';
ALTER LOGIN LoginName WITH PASSWORD = 'NewStrongPassword';
""")
conn.commit()

cursor.execute("""
-- User (Database-Level)
-- DROP USER UserName;
DROP USER IF EXISTS UserName;
CREATE USER UserName FOR LOGIN LoginName;
""")
conn.commit()

cursor.execute("""
-- Server Role (Group at Server-Level)
DROP SERVER ROLE ServerRoleName;
CREATE SERVER ROLE ServerRoleName;
ALTER SERVER ROLE ServerRoleName DROP MEMBER LoginName;
ALTER SERVER ROLE ServerRoleName ADD MEMBER LoginName;
""")
conn.commit()

cursor.execute("""
-- Database Role (Group at Database-Level)
-- DROP ROLE DbRoleName;
DROP ROLE IF EXISTS DbRoleName;
CREATE ROLE DbRoleName;
ALTER ROLE DbRoleName DROP MEMBER UserName;
ALTER ROLE DbRoleName ADD MEMBER UserName;
""")
conn.commit()

select_query = """
-- View Server Logins and Roles
SELECT * FROM sys.server_principals         -- All server-level logins and roles
WHERE name IN ('LoginName', 'ServerRoleName');
SELECT sp.name, role_principal_id, member_principal_id, type, type_desc
FROM sys.server_role_members srm            -- Membership of server roles
INNER JOIN sys.server_principals sp ON role_principal_id = sp.principal_id OR member_principal_id = sp.principal_id
WHERE name IN ('LoginName', 'ServerRoleName')
-- View Database Users and Roles
SELECT * FROM sys.database_principals       -- All users and roles in the database
WHERE type IN ('S', 'U', 'G');
SELECT dp.name, role_principal_id, member_principal_id, type, type_desc
FROM sys.database_role_members srm          -- Membership of database roles
INNER JOIN sys.database_principals dp ON role_principal_id = dp.principal_id OR member_principal_id = dp.principal_id
WHERE dp.type IN ('S', 'U', 'G');
"""

cursor.execute(select_query)

results = []
while True:
    rows = cursor.fetchall()
    if not rows:
        break
    columns = [column[0] for column in cursor.description]
    df = pd.DataFrame.from_records(rows, columns=columns)
    results.append(df)
    if not cursor.nextset():
        break
    
for i, df in enumerate(results, start=1):
    print(f'{i} SELECT STATEMENT\n, {df}\n')
cursor.close()
conn.close()