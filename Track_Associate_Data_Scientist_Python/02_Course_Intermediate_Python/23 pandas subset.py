# Import cars data
import pandas as pd
cars = pd.read_csv('D:\STUDY\python\Course_Intermediate_Python\cars.csv', index_col = 0)

# Print out first 3 observations
print(cars[:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])