"""
merge_asof() and merge_ordered() differences
The merge_asof() and merge_ordered() functions are similar in the type of merge they perform and the input arguments they use. 
In this exercise, think about how the functions are different.
"""

# Drag and drop the statement into the appropriate box for either the merge_asof() function, 
# the merge_ordered() function, or both if it applies to both functions.

# merge_asof()
# After matching two tables, if there are missing values at the top of the table from the right table, this function can fill them in.
# It can be used to do fuzzy matching of dates between tables.

# both
# This function can be used when working with ordered or time-series data.
# This function can set the suffix for overlapping column names.

# merge_ordered
# If it cannot match the rows of the tables exactly, it can use forward fill to interpolate the missing data.
# It allows for a right join during the merge.

# Remarkable work! You were able to identify some of the similarities and differences between the functions. You are well on your way to mastering both!