import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

food_consumption = pd.read_csv(r'D:\STUDY\python\Review\06 statistics\datasets\food_consumption.csv')

# Print variance and sd of co2_emission for each food_category
print(food_consumption.groupby('food_category')['co2_emission'].agg([np.var, np.std]))

# Create histogram of co2_emission for food_category 'beef'
food_consumption[food_consumption['food_category'] == 'beef']['co2_emission'].hist()
plt.show()

# Create histogram of co2_emission for food_category 'eggs'
plt.figure()
food_consumption[food_consumption['food_category'] == 'eggs']['co2_emission'].hist()
plt.show()