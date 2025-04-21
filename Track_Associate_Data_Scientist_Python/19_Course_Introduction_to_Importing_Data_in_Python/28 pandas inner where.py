from sqlalchemy import create_engine, text
import pandas as pd
path = r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\19_Course_Introduction_to_Importing_Data_in_Python\datasets\Chinook.sqlite'
engine = create_engine(f'sqlite:///{path}')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM PlaylistTrack INNER JOIN Track on PlaylistTrack.Trackid = Track.TrackID WHERE Milliseconds < 250000', engine)

# Print head of DataFrame
print(df.head())