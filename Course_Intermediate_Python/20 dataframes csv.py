# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)

#   Unnamed: 0  cars_per_cap        country  drives_right
# 0         US           809  United States          True
# 1        AUS           731      Australia         False
# 2        JPN           588          Japan         False
# 3         IN            18          India         False
# 4         RU           200         Russia          True
# 5        MOR            70        Morocco          True
# 6         EG            45          Egypt          True