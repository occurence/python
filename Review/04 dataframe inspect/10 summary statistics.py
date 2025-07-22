import pandas as pd

sales = pd.read_csv(r'D:\STUDY\python\Review\04 dataframe inspect\sales_subset.csv',index_col=0)

# Print the head of the sales DataFrame
print(sales.head())

# Print the info about the sales DataFrame
print(sales.info())

# Print the mean of weekly_sales
print(sales['weekly_sales'].mean())

# Print the median of weekly_sales
print(sales['weekly_sales'].median())