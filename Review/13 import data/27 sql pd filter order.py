# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
path = r'D:\STUDY\python\Review\13 import data\datasets\Chinook.sqlite'
engine = create_engine(f'sqlite:///{path}')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM Employee WHERE EmployeeId >= 6 ORDER BY BirthDate', engine)

# Print head of DataFrame
print(df.head())
