import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

food_consumption = pd.read_csv(r'D:\STUDY\python\Review\06 statistics\datasets\food_consumption.csv')

# Mean and Median
usa_consumption = food_consumption[food_consumption['country'] == 'USA']
print(np.mean(usa_consumption['consumption']))
print(np.median(usa_consumption['consumption']))

rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']
rice_consumption['co2_emission'].hist()
plt.show()
print(rice_consumption['co2_emission'].agg([np.mean, np.median]))

# Variance and Standard Deviation
print(food_consumption.groupby('food_category')['co2_emission'].agg([np.var, np.std]))
food_consumption[food_consumption['food_category'] == 'beef']['co2_emission'].hist()
plt.show()
plt.figure()
food_consumption[food_consumption['food_category'] == 'eggs']['co2_emission'].hist()
plt.show()

# Quartiles Quintiles Deciles
print(np.quantile(food_consumption['co2_emission'], np.linspace(0, 1, 5)))
print(np.quantile(food_consumption['co2_emission'], np.linspace(0, 1, 6)))
print(np.quantile(food_consumption['co2_emission'], np.linspace(0, 1, 11)))

# Outliers IQR
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()
print(emissions_by_country)
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
outliers = emissions_by_country[(emissions_by_country < lower) | (emissions_by_country > upper)]
print(outliers)

# Probability
counts = food_consumption['food_category'].value_counts()
probs = counts / food_consumption.shape[0]
print(probs)

# Sampling
np.random.seed(24)
sample_without_replacement = food_consumption.sample(5, replace=False)
print(sample_without_replacement)
sample_with_replacement = food_consumption.sample(5, replace=True)
print(sample_with_replacement)