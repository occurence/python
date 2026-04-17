# Import pandas as pd
import pandas as pd

# Read the data from file using read_csv
climate_change = pd.read_csv(r'D:\STUDY\python\Review\07 matplotlib\datasets\climate_change.csv', parse_dates=['date'], index_col='date')

print(climate_change)