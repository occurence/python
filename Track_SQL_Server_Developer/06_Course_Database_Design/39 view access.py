import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=DatabaseDesign;" "Trusted_Connection=True;" )
cursor = conn.cursor()

cursor.execute("""
DROP VIEW IF EXISTS long_reviews;
""")
conn.commit()

cursor.execute("""
CREATE VIEW long_reviews AS
SELECT content.reviewid,
    content.content
   FROM content
  --WHERE (len(content.content) > 4000);
  WHERE DATALENGTH(content.content) > 4000;
""")
conn.commit()

cursor.execute("""
-- Revoke everyone's update and insert privileges
REVOKE UPDATE, INSERT ON long_reviews FROM public;
""")
conn.commit()

cursor.execute("""
-- Grant the editor update and insert privileges 
GRANT UPDATE, INSERT ON long_reviews TO public;
""")
conn.commit()


select_query = """
-- Get all non-systems views
SELECT * FROM information_schema.views
WHERE table_schema not in ('pg_catalog', 'information_schema');

SELECT 
    dp.state_desc AS PermissionState,
    dp.permission_name AS PermissionType,
    pr.name AS Grantee,
    ob.name AS ObjectName,
    ob.type_desc AS ObjectType
FROM 
    sys.database_permissions dp
JOIN 
    sys.objects ob ON dp.major_id = ob.object_id
JOIN 
    sys.database_principals pr ON dp.grantee_principal_id = pr.principal_id
WHERE 
    ob.name = 'long_reviews';
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