import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

food_consumption = pd.read_csv(r'D:\STUDY\python\Review\06 statistics\datasets\food_consumption.csv')

# Calculate the quartiles of co2_emission
print(np.quantile(food_consumption['co2_emission'], np.linspace(0, 1, 5)))

# Calculate the quintiles of co2_emission
print(np.quantile(food_consumption['co2_emission'], np.linspace(0, 1, 6)))

# Calculate the deciles of co2_emission
print(np.quantile(food_consumption['co2_emission'], np.linspace(0, 1, 11)))