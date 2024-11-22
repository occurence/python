import pandas as pd
sales = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\04_Course_Data_Manipulation_Pandas\sales_subset.csv')

# Print the maximum of the date column
print(sales['date'].max())

# Print the minimum of the date column
print(sales['date'].min())