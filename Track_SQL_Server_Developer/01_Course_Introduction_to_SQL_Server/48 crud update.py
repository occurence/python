import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

select_query = """
-- Select the album
SELECT 
  title 
FROM 
  album 
WHERE 
  AlbumId = 213;
"""

update_query = """
-- UPDATE the title of the album
UPDATE 
  album 
SET 
  title = 'Pure Cult: The Best Of The Cult'
WHERE 
  AlbumId = 213;
"""
# Pure Cult: The Best Of The Cult
# Pure Cult: The Best Of The Cult (For Rockers Ravers Lovers & Sinners) UK

df = pd.read_sql(select_query, conn)
print(df)

cursor.execute(update_query)
conn.commit()

df = pd.read_sql(select_query, conn)
print(df)


cursor.close()
conn.close()