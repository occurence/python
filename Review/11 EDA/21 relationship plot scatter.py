import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

divorce = pd.read_csv(r'D:\STUDY\python\Review\11 EDA\datasets\divorce.csv', parse_dates=['divorce_date', 'dob_man', 'dob_woman', 'marriage_date'])
divorce["marriage_year"] = divorce["marriage_date"].dt.year
divorce['man_age_marriage'] = divorce['marriage_year'] - divorce['dob_man'].dt.year
divorce['woman_age_marriage'] = divorce['marriage_year'] - divorce['dob_woman'].dt.year

# Create the scatterplot
sns.scatterplot(data=divorce, x='marriage_duration', y='num_kids')
plt.show()

print(divorce['num_kids'].value_counts())