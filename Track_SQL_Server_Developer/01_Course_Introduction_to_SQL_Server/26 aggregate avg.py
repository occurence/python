import pyodbc
import pandas as pd

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=datacamp;"
    "Trusted_Connection=True;"
)

query = """
-- Find the average number of affected customers
SELECT 
  -- AVG(affected_customers) AS avg_affected_customers
  AVG(CAST (affected_customers AS FLOAT)) AS avg_affected_customers
FROM 
  grid
-- Only retrieve rows where demand_loss_mw has a value
WHERE 
  -- demand_loss_mw IS NOT NULL;
  demand_loss_mw <> '';
"""

df = pd.read_sql(query, conn)
print(df)
conn.close()