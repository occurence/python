import pandas as pd
import numpy as np

food_consumption = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\07_Course_Introduction_Statistics_Python\datasets\food_consumption.csv')

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

# Histogram of co2_emission for rice and show plot
rice_consumption['co2_emission'].hist()
plt.show()

# Calculate mean and median of co2_emission with .agg()
print(rice_consumption['co2_emission'].agg([np.mean, np.median]))