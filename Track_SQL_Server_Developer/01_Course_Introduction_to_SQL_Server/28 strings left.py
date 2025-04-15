import pyodbc
import pandas as pd

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=datacamp;"
    "Trusted_Connection=True;"
)

query = """
-- Select the first 25 characters from the left of the description column
SELECT 
  LEFT(description, 25) AS first_25_left 
FROM 
  grid;
"""

df = pd.read_sql(query, conn)
print(df)
conn.close()