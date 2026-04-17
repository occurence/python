from sqlalchemy import create_engine, text
import pandas as pd
path = r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\19_Course_Introduction_to_Importing_Data_in_Python\datasets\Chinook.sqlite'
engine = create_engine(f'sqlite:///{path}')

# Open engine in context manager
with engine.connect() as con:
    query = text('SELECT * FROM Employee ORDER BY BirthDate')
    rs = con.execute(query)
    df = pd.DataFrame(rs.fetchall())

    # Set the DataFrame's column names
    df.columns = rs.keys()

# Print head of DataFrame
print(df.head())
