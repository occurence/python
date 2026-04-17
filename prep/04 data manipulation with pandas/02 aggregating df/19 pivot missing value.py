"""
Fill in missing values and sum values with pivot tables
The .pivot_table() method has several useful arguments, including fill_value and margins.

fill_value replaces missing values with a real value (known as imputation). What to replace missing values with is a topic big enough to have its own course (Dealing with Missing Data in Python), but the simplest thing to do is to substitute a dummy value.
margins is a shortcut for when you pivoted by two variables, but also wanted to pivot by each of those variables separately: it gives the row and column totals of the pivot table contents.
In this exercise, you'll practice using these arguments to up your pivot table skills, which will help you crunch numbers more efficiently!

sales is available and pandas is imported as pd.
"""

# Print the mean weekly_sales by department and type, filling in any missing values with 0.
# Print the mean weekly_sales by department and type, filling in any missing values with 0 and summing all rows and columns.

import pandas as pd
sales = pd.read_csv(r"D:\STUDY\python\prep\04 data manipulation with pandas\datasets\sales_subset.csv", index_col=0)

# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values='weekly_sales', index='type', columns='department', fill_value=0))

# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0, margins=True))

# Magnificent margin making! 
# You are now armed with pivot table skills that can help you compute summaries at multiple grouped levels in one line of code. 
# Note the subtlety in the value of margins here. 
# The column 'All' returns an overall mean for each department, not (A+B)/2. 
# (A+B)/2 would be a mean of means, rather than an overall mean per department!