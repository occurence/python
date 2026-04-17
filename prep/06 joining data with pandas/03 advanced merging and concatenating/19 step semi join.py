"""
Steps of a semi join
In the last video, you were shown how to perform a semi join with pandas. 
In this exercise, you'll solidify your understanding of the necessary steps. 
Recall that a semi join filters the left table to only the rows where a match exists in both the left and right tables.
"""

# Sort the steps in the correct order of the technique shown to perform a semi join in pandas.

# Merge the left and right tables on key column using an inner join
# Search if the key column in the left table is in the merged tables using the .isin() method creating a boolean series
# Subset the rows of the left table

# Congratulations! You have a sense of the steps in this technique. 
# It first merges the tables, then searches it for which rows belong in the final result creating a filter 
# and subsets the left table with that filter.