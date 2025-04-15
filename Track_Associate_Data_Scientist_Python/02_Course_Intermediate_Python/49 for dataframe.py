# Import cars data
import pandas as pd
cars = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\02_Course_Intermediate_Python\cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows() :
    print(lab)
    print(row)