import seaborn as sns
import pandas as pd
from statsmodels.graphics.gofplots import qqplot
import matplotlib.pyplot as plt

chicken_data = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\30_Course_Experimental_Design_in_Python\datasets\chick_weight.csv')

# Plot the distribution of the chickens' weight
sns.displot(data=chicken_data, x='weight', kind='kde')
plt.show()

# Plot the qq plot of the chickens' weight
qqplot(data=chicken_data['weight'], line='s')
plt.show()

# Subset the data and plot the weight of the subset
subset_data = chicken_data[chicken_data['Time'] == 2]

sns.displot(data=subset_data, x='weight', kind="kde")
plt.show()