import pandas as pd

file = r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\19_Course_Introduction_to_Importing_Data_in_Python\datasets\battledeath.xlsx'
xls = pd.ExcelFile(file)

# Load a sheet into a DataFrame by name: df1
df1 = xls.parse('2004')

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2 = xls.parse(0)

# Print the head of the DataFrame df2
print(df2.head())