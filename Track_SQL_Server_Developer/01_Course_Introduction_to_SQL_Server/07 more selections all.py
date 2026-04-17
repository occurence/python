import pyodbc
import pandas as pd

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=datacamp;"
    "Trusted_Connection=True;"
)

query = """
-- Amend the code to select all columns
SELECT 
  *
FROM 
  eurovision;
"""

df = pd.read_sql(query, conn)
print(df)
conn.close()