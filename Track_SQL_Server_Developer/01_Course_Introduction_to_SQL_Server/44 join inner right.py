import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )

query = """
SELECT 
  album.AlbumId,
  title,
  album.ArtistId,
  artist.name as artist
FROM album
INNER JOIN artist ON album.ArtistId = artist.ArtistId
-- Perform the correct join type to return matches or NULLS from the track table
RIGHT JOIN track on album.AlbumId = track.AlbumId
WHERE album.AlbumId IN (213,214)
"""

df = pd.read_sql(query, conn)
print(df)
conn.close()