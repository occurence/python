import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

planes = pd.read_csv(r'D:\STUDY\python\Review\11 EDA\datasets\planes.csv')

# Plot a histogram of flight prices
sns.histplot(data=planes, x="Price")
plt.show()

# Display descriptive statistics for flight duration
print(planes['Duration'].describe())

sns.boxplot(data=planes, y='Price')
plt.show()

sns.boxplot(data=planes, x='Duration')
plt.show()