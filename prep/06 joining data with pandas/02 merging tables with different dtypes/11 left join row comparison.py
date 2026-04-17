"""
How many rows with a left join?
Select the true statement about left joins.

Try running the following code statements:

left_table.merge(one_to_one, on='id', how='left').shape
left_table.merge(one_to_many, on='id', how='left').shape
Note that the left_table starts out with 4 rows.
"""

# Possible answers

# The output of a one-to-one merge with a left join will have more rows than the left table.
# The output of a one-to-one merge with a left join will have fewer rows than the left table.
# The output of a one-to-many merge with a left join will have greater than or equal rows than the left table.



import pandas as pd
left_table = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\movies.csv', index_col=0)
left_table = left_table[left_table['title'].str.contains('Jurassic')]
one_to_one = pd.read_pickle(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\taglines.p')[['id','tagline']]
one_to_many = pd.read_pickle(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\crews.p')[['id','job','name']]

print(left_table.merge(one_to_one, on='id', how='left').shape)
print(left_table.merge(one_to_one, on='id', how='left'))
print(left_table.merge(one_to_many, on='id', how='left').shape)
print(left_table.merge(one_to_many, on='id', how='left'))

# That's correct! 
# A left join will return all of the rows from the left table. 
# If those rows in the left table match multiple rows in the right table, then all of those rows will be returned. 
# Therefore, the returned rows must be equal to if not greater than the left table. 
# Knowing what to expect is useful in troubleshooting any suspicious merges.