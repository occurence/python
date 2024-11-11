# Import cars data
import pandas as pd
cars = pd.read_csv('D:\STUDY\python\Course_Intermediate_Python\cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows() :
    print(lab)
    print(row)