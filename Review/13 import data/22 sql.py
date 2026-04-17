path = r'D:\STUDY\python\Review\13 import data\datasets\Chinook.sqlite'

# Import packages
from sqlalchemy import create_engine, text
import pandas as pd

# Create engine: engine
engine = create_engine(f'sqlite:///{path}')

# Open engine connection: con
con = engine.connect()

# Perform query: rs
# rs = con.execute('SELECT * FROM Album')
rs = con.execute(text('SELECT * FROM Album'))

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())

# Close connection
con.close()

# Print head of DataFrame df
print(df.head())
