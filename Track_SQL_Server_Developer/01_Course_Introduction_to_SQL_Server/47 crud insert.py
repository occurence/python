import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

create_insert_query = """
DROP TABLE IF EXISTS tracks;
-- Create the table
CREATE TABLE tracks(
  -- Create track column
  track VARCHAR(200), 
  -- Create album column
  album VARCHAR(160), 
  -- Create track_length_mins column
  track_length_mins INT
);
-- Complete the statement to enter the data to the table         
INSERT INTO tracks
-- Specify the destination columns
(track, album, track_length_mins)
-- Insert the appropriate values for track, album and track length
VALUES
  ('Basket Case', 'Dookie', 3);
"""
cursor.execute(create_insert_query)
conn.commit()

select_query = """
-- Select all columns from the new table
SELECT 
  *
FROM 
  tracks;
"""

df = pd.read_sql(select_query, conn)
print(df)
cursor.close()
conn.close()