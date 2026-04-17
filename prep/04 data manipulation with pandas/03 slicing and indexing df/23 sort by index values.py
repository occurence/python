"""
Sorting by index values
Previously, you changed the order of the rows in a DataFrame by calling .sort_values(). It's also useful to be able to sort by elements in the index. For this, you need to use .sort_index().

pandas is loaded as pd. temperatures_ind has a multi-level index of country and city, and is available.
"""

# Sort temperatures_ind by the index values.
# Sort temperatures_ind by the index values at the "city" level.
# Sort temperatures_ind by ascending country then descending city.

import pandas as pd
temperatures = pd.read_csv(r"D:\STUDY\python\prep\04 data manipulation with pandas\datasets\temperatures.csv")
temperatures_ind = temperatures.set_index(['country','city'])

print(temperatures_ind.head())

# Sorted! 
# Sorting index values is similar to sorting values in columns, 
# except that you call .sort_index() instead of .sort_values().