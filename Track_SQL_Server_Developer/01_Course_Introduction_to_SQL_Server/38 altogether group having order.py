import pyodbc
import pandas as pd

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=datacamp;"
    "Trusted_Connection=True;"
)

query = """
SELECT 
  country, 
  COUNT(country) AS country_count, 
  -- AVG (place) AS avg_place, 
  AVG(CAST(place AS FLOAT)) AS avg_place, 
  AVG(CAST(place AS FLOAT)) AS avg_points, 
  MIN(points) AS min_points, 
  MAX(points) AS max_points 
FROM 
  eurovision 
GROUP BY 
  country 
  -- The country column should only contain those with a count greater than 5
HAVING 
  COUNT(country) > 5 
  -- Arrange columns in the correct order
ORDER BY 
  avg_place, 
  avg_points DESC;
"""

df = pd.read_sql(query, conn)
print(df)
conn.close()