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
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars)
print(cars['drives_right'])
# Print out drives_right column as DataFrame
print(cars[['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars[['cars_per_cap','drives_right']])