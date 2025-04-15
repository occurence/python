import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

divorce = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\14_Course_Exploratory_Data_Analysis_in_Python\datasets\divorce.csv', parse_dates=['marriage_date'])

# Create a pairplot for income_woman and marriage_duration
sns.pairplot(data=divorce, vars=['income_woman', 'marriage_duration'])
plt.show()