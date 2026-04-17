import pyodbc
import pandas as pd

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=datacamp;"
    "Trusted_Connection=True;"
)

query = """
-- Select country and event_year from eurovision
SELECT 
  country, 
  event_year 
FROM 
  eurovision;
"""

df = pd.read_sql(query, conn)
print(df)
conn.close()