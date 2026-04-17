import pyodbc
import pandas as pd

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=datacamp;"
    "Trusted_Connection=True;"
)

query = """
-- Select nerc_region and demand_loss_mw
SELECT 
  nerc_region, 
  demand_loss_mw 
FROM 
  grid 
-- Retrieve rows where affected_customers is >= 500000  (500,000)
WHERE 
  affected_customers >= 500000;
"""

df = pd.read_sql(query, conn)
print(df)
conn.close()