import pandas as pd
sales = pd.read_csv(r'D:\STUDY\python\Course_Data_Manipulation_Pandas\sales_subset.csv')

# Print the head of the sales DataFrame
print(sales.head())

# Print the info about the sales DataFrame
print(sales.info())

# Print the mean of weekly_sales
print(sales['weekly_sales'].mean())

# Print the median of weekly_sales
print(sales['weekly_sales'].median())