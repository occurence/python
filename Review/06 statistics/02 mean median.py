import pandas as pd

food_consumption = pd.read_csv(r'D:\STUDY\python\Review\06 statistics\datasets\food_consumption.csv')

# Import numpy with alias np
import numpy as np

# Subset country for USA: usa_consumption
usa_consumption = food_consumption[food_consumption['country'] == 'USA']

# Calculate mean consumption in USA
print(np.mean(usa_consumption['consumption']))

# Calculate median consumption in USA
print(np.median(usa_consumption['consumption']))