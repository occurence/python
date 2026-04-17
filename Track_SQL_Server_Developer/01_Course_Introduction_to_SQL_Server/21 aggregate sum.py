import pyodbc
import pandas as pd

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=datacamp;"
    "Trusted_Connection=True;"
)

query = """
-- Sum the demand_loss_mw column
SELECT 
  -- SUM(demand_loss_mw) AS MRO_demand_loss
  SUM(CAST(demand_loss_mw AS FLOAT)) AS MRO_demand_loss
FROM 
  grid 
WHERE
  -- demand_loss_mw should not contain NULL values
  demand_loss_mw IS NOT NULL 
  -- and nerc_region should be 'MRO';
  AND nerc_region = 'MRO';
"""

df = pd.read_sql(query, conn)
print(df)
conn.close()