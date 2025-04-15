import pyodbc
import pandas as pd

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=datacamp;"
    "Trusted_Connection=True;"
)

query = """
-- Calculate the length of the description column
SELECT 
  LEN (description) AS description_length 
FROM 
  grid;
"""

df = pd.read_sql(query, conn)
print(df)
conn.close()