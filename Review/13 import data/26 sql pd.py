# Import packages
from sqlalchemy import create_engine, text
import pandas as pd

# Create engine: engine
path = r'D:\STUDY\python\Review\13 import data\datasets\Chinook.sqlite'
engine = create_engine(f'sqlite:///{path}')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM Album', engine)

# Print head of DataFrame
print(df.head())

# Open engine in context manager and store query result in df1
with engine.connect() as con:
    rs = con.execute(text("SELECT * FROM Album"))
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

# Confirm that both methods yield the same result
print(df.equals(df1))