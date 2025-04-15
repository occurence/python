# Import packages
from sqlalchemy import create_engine, text
import pandas as pd
path = r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\19_Course_Introduction_to_Importing_Data_in_Python\datasets\Chinook.sqlite'


# Create engine: engine
engine = create_engine(f'sqlite:///{path}')

# Open engine connection: con
con = engine.connect()

# Perform query: rs
# rs = con.execute('SELECT * FROM Album')
query = text('SELECT * FROM Album')
rs = con.execute(query)

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())

# Close connection
con.close()

# Print head of DataFrame df
print(df.head())
