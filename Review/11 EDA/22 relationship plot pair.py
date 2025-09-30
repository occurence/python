import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

divorce = pd.read_csv(r'D:\STUDY\python\Review\11 EDA\datasets\divorce.csv', parse_dates=['divorce_date', 'dob_man', 'dob_woman', 'marriage_date'])
divorce["marriage_year"] = divorce["marriage_date"].dt.year
divorce['man_age_marriage'] = divorce['marriage_year'] - divorce['dob_man'].dt.year
divorce['woman_age_marriage'] = divorce['marriage_year'] - divorce['dob_woman'].dt.year

# Create a pairplot for income_woman and marriage_duration
sns.pairplot(data=divorce, vars=['income_woman' , 'marriage_duration'])
plt.show()

sns.pairplot(data=divorce)
plt.show()