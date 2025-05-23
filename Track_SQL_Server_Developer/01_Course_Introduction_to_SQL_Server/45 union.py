import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )

query = """
SELECT 
  AlbumId AS ID,
  title AS description,
  'Album' AS Source
  -- Complete the FROM statement
FROM album
 -- Combine the result set using the relevant keyword
UNION
SELECT 
  ArtistId AS ID,
  name AS description,
  'Artist'  AS Source
  -- Complete the FROM statement
FROM artist;
"""

df = pd.read_sql(query, conn)
print(df)
conn.close()