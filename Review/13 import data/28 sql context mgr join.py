from sqlalchemy import create_engine, text
import pandas as pd

path = r'D:\STUDY\python\Review\13 import data\datasets\Chinook.sqlite'
engine = create_engine(f'sqlite:///{path}')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute(text('SELECT Title, Name FROM Album INNER JOIN Artist ON Album.ArtistID = Artist.ArtistID'))
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print head of DataFrame df
print(df.head())
