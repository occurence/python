# Import cars data
import pandas as pd
cars = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\02_Course_Intermediate_Python\cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, 'COUNTRY'] = row['country'].upper()

# Print cars
print(cars)