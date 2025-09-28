import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

unemployment = pd.read_csv(r'D:\STUDY\python\Review\11 EDA\datasets\clean_unemployment.csv')

# Print the minimum and maximum unemployment rates during 2021
print(unemployment['2021'].min(), unemployment['2021'].max())

# Create a boxplot of 2021 unemployment rates, broken down by continent
sns.boxplot(data=unemployment, x='2021', y='continent')
plt.show()

sns.histplot(data=unemployment, x='2021', y='continent')
plt.show()