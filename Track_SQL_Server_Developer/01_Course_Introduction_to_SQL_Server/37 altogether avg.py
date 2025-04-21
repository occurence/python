import pyodbc
import pandas as pd

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=datacamp;"
    "Trusted_Connection=True;"
)

query = """
-- Obtain a count for each country
SELECT 
  COUNT(country) AS country_count, 
  -- Retrieve the country column
  country, 
  -- Return the average of the Place column 
  -- AVG(place) AS average_place, 
  AVG(CAST(place AS FLOAT)) AS average_place, 
  -- AVG(points) AS avg_points, 
  AVG(CAST(points AS FLOAT)) AS avg_points, 
  MIN(points) AS min_points, 
  MAX(points) AS max_points 
FROM 
  eurovision 
GROUP BY 
  country;
"""

df = pd.read_sql(query, conn)
print(df)
conn.close()