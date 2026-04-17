import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )

query = """
-- SELECT the fully qualified album_id column from the album table
SELECT 
  AlbumId,
  title,
  album.ArtistId,
  -- SELECT the fully qualified name column from the artist table
  name as artist
FROM album
-- Perform a join to return only rows that match from both tables
INNER JOIN artist ON album.ArtistId = artist.ArtistId
WHERE album.AlbumId IN (213,214)
"""

df = pd.read_sql(query, conn)
print(df)
conn.close()