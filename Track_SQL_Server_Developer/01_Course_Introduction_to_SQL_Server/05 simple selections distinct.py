import pyodbc
import pandas as pd

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=datacamp;"
    "Trusted_Connection=True;"
)

query = """
-- Return unique countries and use an alias
SELECT 
  DISTINCT country AS unique_country 
FROM 
  eurovision;
"""

df = pd.read_sql(query, conn)
print(df)
conn.close()