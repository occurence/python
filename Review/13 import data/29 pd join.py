from sqlalchemy import create_engine, text
import pandas as pd

path = r'D:\STUDY\python\Review\13 import data\datasets\Chinook.sqlite'
engine = create_engine(f'sqlite:///{path}')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000', engine)

# Print head of DataFrame
print(df.head())