import pandas as pd

sales_df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\10_Course_Dimensionality_Reduction_in_Python\datasets\sales_df.csv')

# Calculate the price from the quantity sold and revenue
sales_df['price'] = sales_df['revenue']/sales_df['quantity']

# Drop the quantity and revenue features
reduced_df = sales_df.drop(['quantity','revenue'], axis=1)

print(reduced_df.head())