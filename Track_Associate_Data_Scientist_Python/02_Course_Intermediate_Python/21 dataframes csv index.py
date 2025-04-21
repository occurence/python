# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('D:\STUDY\python\Course_Intermediate_Python\cars.csv', index_col=0)

# Print out cars
print(cars)