#      cars_per_cap        country  drives_right
# US            809  United States          True
# AUS           731      Australia         False
# JPN           588          Japan         False
# IN             18          India         False
# RU            200         Russia          True
# MOR            70        Morocco          True
# EG             45          Egypt          True

# Import cars data
import pandas as pd
cars = pd.read_csv('D:\STUDY\python\Course_Intermediate_Python\cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country','drives_right']])