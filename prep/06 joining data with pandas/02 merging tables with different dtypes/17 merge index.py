"""
Index merge for movie ratings
To practice merging on indexes, you will merge movies and a table called ratings that holds info about movie ratings. Ensure that your merge returns all rows from the movies table, and only matching rows from the ratings table.

The movies and ratings tables have been loaded for you.
"""

# Merge the movies and ratings tables on the id column, keeping all rows from the movies table, and save the result as movies_ratings.

import pandas as pd

movies = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\movies.csv', index_col=1).drop(columns='Unnamed: 0',axis=1)
ratings = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\ratings.csv', index_col=1).drop(columns='Unnamed: 0',axis=1)

print(movies.head())
print(ratings.head())

# Merge to the movies table the ratings table on the index
movies_ratings = movies.merge(ratings, how='left', left_on='id', right_index=True)

# Print the first few rows of movies_ratings
print(movies_ratings.head())

# Good work! 
# Merging on indexes is just like merging on columns, so if you need to merge based on indexes, 
# there's no need to turn the indexes into columns first.