# Import necessary module
from sqlalchemy import create_engine, inspect

path = r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\19_Course_Introduction_to_Importing_Data_in_Python\datasets\Chinook.sqlite'


# Create engine: engine
engine = create_engine(f'sqlite:///{path}')
# print(engine.table_names())
inspector = inspect(engine)
print(inspector.get_table_names())