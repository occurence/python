"""
Counting categorical variables
Counting is a great way to get an overview of your data and to spot curiosities that you might not notice otherwise. In this exercise, you'll count the number of each type of store and the number of each department number using the DataFrames you created in the previous exercise:

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=["store", "type"])

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=["store", "department"])
The store_types and store_depts DataFrames you created in the last exercise are available, and pandas is imported as pd.
"""

# Count the number of stores of each store type in store_types.
# Count the proportion of stores of each store type in store_types.
# Count the number of stores of each department in store_depts, sorting the counts in descending order.
# Count the proportion of stores of each department in store_depts, sorting the proportions in descending order.

import pandas as pd
sales = pd.read_csv(r"D:\STUDY\python\prep\04 data manipulation with pandas\datasets\sales_subset.csv", index_col=0)
store_types = sales.drop_duplicates(subset=['store','type'])
store_depts = sales.drop_duplicates(subset=['store','department'])

# Count the number of stores of each type
store_counts = store_types['type'].value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types['type'].value_counts(normalize=True)
print(store_props)

# Count the number of stores for each department and sort
dept_counts_sorted = store_depts['department'].value_counts(sort=True)
print(dept_counts_sorted)

# Get the proportion of stores in each department and sort
dept_props_sorted = store_depts['department'].value_counts(sort=True, normalize=True)
print(dept_props_sorted)

# Great counting! 
# It looks like department 43 only exists in two stores.