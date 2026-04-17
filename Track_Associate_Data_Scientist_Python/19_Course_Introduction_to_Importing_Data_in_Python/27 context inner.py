from sqlalchemy import create_engine, text
import pandas as pd
path = r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\19_Course_Introduction_to_Importing_Data_in_Python\datasets\Chinook.sqlite'
engine = create_engine(f'sqlite:///{path}')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute(text('SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistID = Artist.ArtistID'))
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print head of DataFrame df
print(df.head())
