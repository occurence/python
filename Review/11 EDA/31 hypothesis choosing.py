import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

salaries = pd.read_csv(r'D:\STUDY\python\Review\11 EDA\datasets\salaries_response.csv', parse_dates=['date_of_response'])

# Create a bar plot of salary versus company size, factoring in employment status
sns.barplot(data=salaries, x="Company_Size", y="Salary_USD", hue="Employment_Status")
plt.show()

print("On average, large companies pay contractors more than medium-sized companies.")