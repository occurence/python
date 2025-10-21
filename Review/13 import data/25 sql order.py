from sqlalchemy import create_engine, text
import pandas as pd

# Create engine: engine
path = r'D:\STUDY\python\Review\13 import data\datasets\Chinook.sqlite'
engine = create_engine(f'sqlite:///{path}')

# Open engine in context manager
with engine.connect() as con:
    rs = con.execute(text('SELECT * FROM Employee ORDER BY BirthDate'))
    df = pd.DataFrame(rs.fetchall())

    # Set the DataFrame's column names
    df.columns = rs.keys()

# Print head of DataFrame
print(df.head())
