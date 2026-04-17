import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

salaries = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\14_Course_Exploratory_Data_Analysis_in_Python\datasets\salaries_response.csv', parse_dates=['date_of_response'])

# Get the month of the response
salaries["month"] = salaries["date_of_response"].dt.month

# Extract the weekday of the response
salaries["weekday"] = salaries['date_of_response'].dt.weekday

# Create a heatmap
# sns.heatmap(salaries.corr(), annot=True)
numeric_cols = salaries.select_dtypes(include=['number'])
# sns.heatmap(numeric_cols.corr(), annot=True, cmap="coolwarm")
sns.heatmap(numeric_cols.corr(), annot=True)

plt.show()