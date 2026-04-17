import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

salaries = pd.read_csv(r'D:\STUDY\python\Review\11 EDA\datasets\salaries_response.csv', parse_dates=['date_of_response'])

# Get the month of the response
salaries["month"] = salaries["date_of_response"].dt.month

# Extract the weekday of the response
salaries["weekday"] = salaries['date_of_response'].dt.weekday

# Create a heatmap
sns.heatmap(salaries.corr(numeric_only=True), annot=True)
plt.show()