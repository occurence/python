# Import necessary module
from sqlalchemy import create_engine, inspect

path = r'D:\STUDY\python\Review\13 import data\datasets\Chinook.sqlite'

# Create engine: engine
engine = create_engine(f'sqlite:///{path}')
engine = inspect(engine)

# Save the table names to a list: table_names
# table_names = engine.table_names()
table_names = engine.get_table_names()

# Print the table names to the shell
print(table_names)