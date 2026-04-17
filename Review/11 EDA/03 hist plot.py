import pandas as pd

unemployment = pd.read_csv(r'D:\STUDY\python\Review\11 EDA\datasets\clean_unemployment.csv')

# Import the required visualization libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Create a histogram of 2021 unemployment; show a full percent in each bin
# sns.histplot(data=unemployment['2021'])
sns.histplot(data=unemployment, x='2021', binwidth=1)
plt.show()