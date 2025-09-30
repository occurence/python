import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

divorce = pd.read_csv(r'D:\STUDY\python\Review\11 EDA\datasets\divorce.csv', parse_dates=['divorce_date', 'dob_man', 'dob_woman', 'marriage_date'])
divorce["marriage_year"] = divorce["marriage_date"].dt.year
divorce['man_age_marriage'] = divorce['marriage_year'] - divorce['dob_man'].dt.year
divorce['woman_age_marriage'] = divorce['marriage_year'] - divorce['dob_woman'].dt.year

print(divorce.dtypes)
print(divorce.info())
print(divorce.columns)
print(divorce.head())
print(divorce['num_kids'].value_counts(dropna=False))

# Create the scatter plot
sns.scatterplot(data=divorce, x='woman_age_marriage', y='income_woman', hue='education_woman')
plt.show()