import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

divorce = pd.read_csv(r'D:\STUDY\python\Review\11 EDA\datasets\divorce.csv', parse_dates=['divorce_date', 'dob_man', 'dob_woman', 'marriage_date'])
divorce["marriage_year"] = divorce["marriage_date"].dt.year
divorce['man_age_marriage'] = divorce['marriage_year'] - divorce['dob_man'].dt.year
divorce['woman_age_marriage'] = divorce['marriage_year'] - divorce['dob_woman'].dt.year

# Update the KDE plot so that marriage duration can't be smoothed too far
# Update the KDE plot to show a cumulative distribution function
sns.kdeplot(data=divorce, x="marriage_duration", hue="num_kids", cut=0, cumulative=True)
plt.show()