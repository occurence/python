import pyodbc
import pandas as pd

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=datacamp;"
    "Trusted_Connection=True;"
)

query = """
-- Limit the number of rows returned
SELECT 
  TOP (50) country 
FROM 
  eurovision;
"""

df = pd.read_sql(query, conn)
print(df)
conn.close()