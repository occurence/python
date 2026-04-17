import pyodbc
import pandas as pd

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=datacamp;"
    "Trusted_Connection=True;"
)

query = """
-- Select the first 20 rows from the specified columns
SELECT 
  TOP (20) description, 
  event_date 
FROM 
  grid 
  -- Order your results by the event_date column
ORDER BY event_date;
"""

df = pd.read_sql(query, conn)
print(df)
conn.close()