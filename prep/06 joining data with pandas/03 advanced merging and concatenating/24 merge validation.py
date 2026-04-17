"""
Validating a merge
You have been given 2 tables, artists, and albums. 
Merge them using artists.merge(albums, on='artid').head(), adjusting the validate argument to determine which statement is False.
"""

import pandas as pd

artists = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\artists.csv', index_col=0)
albums = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\albums.csv', index_col=0)

print(artists.merge(albums, on='artid', validate='many_to_many'))
print(artists.merge(albums, on='artid', validate='one_to_many'))
print(artists.merge(albums, on='artid', validate='many_to_one'))

# Possible answers

# You can use 'many_to_many' without an error, since there is a duplicate key in one of the tables.
# You can use 'one_to_many' without error, since there is a duplicate key in the right table.
# You can use 'many_to_one' without an error, since there is a duplicate key in the left table. # Correct

# That's correct! 
# This statement is false. 
# There is a duplicate value in the artid column in the albums table, which is the right table in this merge. 
# Therefore, setting validate equal to 'many_to_one' or 'one_to_one' will raise an error, making this statement false.