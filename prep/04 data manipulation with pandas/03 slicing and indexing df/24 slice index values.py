"""
Slicing index values
Slicing lets you select consecutive elements of an object using first:last syntax. DataFrames can be sliced by index values or by row/column number; we'll start with the first case. This involves slicing inside the .loc[] method.

Compared to slicing lists, there are a few things to remember.

You can only slice an index if the index is sorted (using .sort_index()).
To slice at the outer level, first and last can be strings.
To slice at inner levels, first and last should be tuples.
If you pass a single slice to .loc[], it will slice the rows.
pandas is loaded as pd. temperatures_ind has country and city in the index, and is available.
"""

# Sort the index of temperatures_ind.
# Use slicing with .loc[] to get these subsets:
# from Pakistan to Philippines.
# from Lahore to Manila. (This will return nonsense.)
# from Pakistan, Lahore to Philippines, Manila.

import pandas as pd
temperatures = pd.read_csv(r"D:\STUDY\python\prep\04 data manipulation with pandas\datasets\temperatures.csv")
temperatures_ind = temperatures.set_index(['country','city'])

# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Philippines
print(temperatures_srt.loc['Pakistan':'Philippines'])

# Try to subset rows from Lahore to Manila
print(temperatures_srt.loc['Lahore':'Manila'])

# Subset rows from Pakistan, Lahore to Philippines, Manila
print(temperatures_srt.loc[('Pakistan','Lahore'):('Philippines','Manila')])

# That's a nice slice! 
# Combining slicing with .loc[] provides a concise syntax for subsetting.