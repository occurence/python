from sqlalchemy import create_engine, text
import pandas as pd
path = r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\19_Course_Introduction_to_Importing_Data_in_Python\datasets\Chinook.sqlite'
engine = create_engine(f'sqlite:///{path}')


# Execute query and store records in DataFrame: df
query = text('SELECT * FROM Album')
df = pd.read_sql_query(query, engine)

# Print head of DataFrame
print(df.head())

# Open engine in context manager and store query result in df1
with engine.connect() as con:
    rs = con.execute(query)
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

# Confirm that both methods yield the same result
print(df.equals(df1))