import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

select_query = """
-- Select the album
SELECT 
  * 
FROM 
  album
WHERE
  AlbumId = 1000
"""

insert_query = """
-- Complete the statement to enter the data to the table         
INSERT INTO album
-- Specify the destination columns
(AlbumId, Title, ArtistId)
-- Insert the appropriate values for album id, title and artist id
VALUES
  (1000, 'For Those About To Rock We Salute You', 1);
"""

delete_query = """
-- DELETE the record
DELETE FROM 
  album 
WHERE 
  AlbumId = 1000
"""

df = pd.read_sql(select_query, conn)
print(df)

cursor.execute(insert_query)
conn.commit()

df = pd.read_sql(select_query, conn)
print(df)

cursor.execute(delete_query)
conn.commit()

df = pd.read_sql(select_query, conn)
print(df)

cursor.close()
conn.close()