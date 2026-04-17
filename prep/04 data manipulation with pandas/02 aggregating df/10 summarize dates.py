"""
Summarizing dates
Summary statistics can also be calculated on date columns that have values with the data type datetime64. Some summary statistics — like mean — don't make a ton of sense on dates, but others are super helpful, for example, minimum and maximum, which allow you to see what time range your data covers.

sales is available and pandas is loaded as pd.
"""

# Print the maximum of the date column.
# Print the minimum of the date column.

import pandas as pd
sales = pd.read_csv(r"D:\STUDY\python\prep\04 data manipulation with pandas\datasets\sales_subset.csv", index_col=0)

# Print the maximum of the date column
print(sales['date'].max())

# Print the minimum of the date column
print(sales['date'].min())

# Super summarizing! 
# Taking the minimum and maximum of a column of dates is handy for figuring out what time period your data covers. 
# In this case, there are data from February of 2010 to October of 2012.