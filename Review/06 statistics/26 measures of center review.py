import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

food_consumption = pd.read_csv(r'D:\STUDY\python\Review\06 statistics\datasets\food_consumption.csv')

# Subset country for USA: usa_consumption
usa_consumption = food_consumption[food_consumption['country'] == 'USA']

# Calculate mean consumption in USA
print(np.mean(usa_consumption['consumption']))

# Calculate median consumption in USA
print(np.median(usa_consumption['consumption']))

import matplotlib.pyplot as plt
usa_consumption['consumption'].hist()
plt.show()

data = usa_consumption['consumption']

# Calculate mean and median
mean_val = np.mean(data)
median_val = np.median(data)

# Plot histogram
plt.hist(data, edgecolor="black", alpha=0.7)

# Add vertical lines
plt.axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_val:.2f}')
plt.axvline(median_val, color='blue', linestyle='-', linewidth=2, label=f'Median: {median_val:.2f}')

# Add legend
plt.legend()
plt.title("USA Consumption: Histogram with Mean & Median")
plt.xlabel("Consumption")
plt.ylabel("Frequency")

plt.show()


import seaborn as sns

sns.histplot(data, kde=True)
plt.axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_val:.2f}')
plt.axvline(median_val, color='blue', linestyle='-', linewidth=2, label=f'Median: {median_val:.2f}')

plt.legend()
plt.show()