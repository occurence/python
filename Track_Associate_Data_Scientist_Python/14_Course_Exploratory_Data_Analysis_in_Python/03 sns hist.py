# Import the required visualization libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

unemployment = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\14_Course_Exploratory_Data_Analysis_in_Python\datasets\clean_unemployment.csv')

# Create a histogram of 2021 unemployment; show a full percent in each bin
sns.histplot(x='2021', data=unemployment, binwidth=1)
plt.show()