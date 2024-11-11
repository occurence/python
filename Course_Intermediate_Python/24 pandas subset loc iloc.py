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
print(cars)
# Print out observation for Japan
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.iloc[[1,6]])