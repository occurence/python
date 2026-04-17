"""
One-to-many merge
A business may have one or multiple owners. In this exercise, you will continue to gain experience with one-to-many merges by merging a table of business owners, called biz_owners, to the licenses table. Recall from the video lesson, with a one-to-many relationship, a row in the left table may be repeated if it is related to multiple rows in the right table. In this lesson, you will explore this further by finding out what is the most common business owner title. (i.e., secretary, CEO, or vice president)

The licenses and biz_owners DataFrames are loaded for you.
"""

# Starting with the licenses table on the left, merge it to the biz_owners table on the column account, and save the results to a variable named licenses_owners.
# Group licenses_owners by title and count the number of accounts for each title. Save the result as counted_df
# Sort counted_df by the number of accounts in descending order, and save this as a variable named sorted_df.
# Use the .head() method to print the first few rows of the sorted_df.

import pandas as pd
licenses = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\licenses.csv')
biz_owners = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\business_owners.csv')


# Merge the licenses and biz_owners table on account
licenses_owners = licenses.merge(biz_owners, on='account')

# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby('title').agg({'account':'count'})
# counted_df = licenses_owners.groupby('title')['account'].count().reset_index()

# Sort the counted_df in descending order
sorted_df = counted_df.sort_values('account', ascending=False)

# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head())

# Wonderful! 
# After merging the tables together, 
# you counted the number of repeated rows with the combination of .groupby() and .agg() statements. 
# You see that president, followed by secretary, are the most common business owner titles.