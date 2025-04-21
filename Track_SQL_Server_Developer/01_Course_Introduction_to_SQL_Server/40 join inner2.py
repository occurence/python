import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )

query = """
-- Select album_id and title from album, and name from artist
SELECT 
  AlbumId,
  title,
  name AS artist
  -- Enter the main source table name
FROM artist
  -- Perform the inner join
INNER JOIN album on artist.ArtistId = album.ArtistId;
"""

df = pd.read_sql(query, conn)
print(df)
conn.close()