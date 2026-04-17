import pyodbc
import pandas as pd

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=datacamp;"
    "Trusted_Connection=True;"
)

query = """
-- Retrieve the song,artist and release_year columns
SELECT 
  song, 
  artist, 
  release_year 
FROM 
  songlist 
  -- Ensure there are no missing or unknown values in the release_year column
WHERE 
  -- release_year IS NOT NULL 
  release_year <> ''
  -- Arrange the results by the artist and release_year columns
ORDER BY 
  artist, 
  release_year;
"""

df = pd.read_sql(query, conn)
print(df)
conn.close()