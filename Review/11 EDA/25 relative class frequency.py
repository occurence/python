import pandas as pd

salaries = pd.read_csv(r'D:\STUDY\python\Review\11 EDA\datasets\salaries.csv')

# Print the relative frequency of Job_Category
print(salaries['Job_Category'].value_counts(normalize=True))