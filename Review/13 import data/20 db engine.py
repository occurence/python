# Import necessary module
from sqlalchemy import create_engine

path = r'D:\STUDY\python\Review\13 import data\datasets\Chinook.sqlite'

# Create engine: engine
engine = create_engine(f'sqlite:///{path}')