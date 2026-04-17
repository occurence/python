import pyodbc
import pandas as pd

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=datacamp;"
    "Trusted_Connection=True;"
)

query = """
-- Find the minimum number of affected customers
SELECT 
  MIN(affected_customers) AS min_affected_customers 
FROM 
  grid
-- Only retrieve rows where demand_loss_mw has a value
WHERE
  --demand_loss_mw IS NOT NULL;
  demand_loss_mw <> '';
"""

df = pd.read_sql(query, conn)
print(df)
conn.close()