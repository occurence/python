import pyodbc
import pandas as pd

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=datacamp;"
    "Trusted_Connection=True;"
)

query = """
-- Complete the query to find `Weather` within the description column
SELECT 
  description, 
  CHARINDEX('Weather', description) 
FROM 
  grid
WHERE description LIKE '%Weather%';
"""

df = pd.read_sql(query, conn)
print(df)
conn.close()