import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

cursor.execute("""
USE master;
""")
conn.commit()

cursor.execute("""
IF DB_ID('DatabaseDesign') IS NOT NULL
BEGIN
    ALTER DATABASE DatabaseDesign SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE DatabaseDesign;
END
""")
conn.commit()

cursor.execute("""
DROP DATABASE IF EXISTS DatabaseDesign;
CREATE DATABASE DatabaseDesign;
""")
conn.commit()

select_query = """
SELECT name, database_id, create_date
FROM sys.databases
WHERE name = 'DatabaseDesign';
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