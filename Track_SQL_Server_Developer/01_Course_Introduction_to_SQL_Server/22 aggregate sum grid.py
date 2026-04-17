import pyodbc
import pandas as pd

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=datacamp;"
    "Trusted_Connection=True;"
)

query = """
-- Obtain a count of 'grid_id'
SELECT 
  COUNT(grid_id) AS grid_total 
FROM 
  grid;
"""

df = pd.read_sql(query, conn)
print(df)
conn.close()