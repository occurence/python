import pandas as pd

salaries = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\14_Course_Exploratory_Data_Analysis_in_Python\datasets\salaries.csv')

# Print the relative frequency of Job_Category
print(salaries['Job_Category'].value_counts(normalize=True))