import pandas as pd

movies = pd.read_pickle(r'D:\STUDY\python\Review\05 join pandas\datasets\movies.p')
movies.set_index(movies.columns[0], inplace=True)
ratings = pd.read_pickle(r'D:\STUDY\python\Review\05 join pandas\datasets\ratings.p')
ratings.set_index(ratings.columns[0], inplace=True)

# Merge to the movies table the ratings table on the index
# movies_ratings = movies.merge(ratings, how='left', left_on='id', right_index=True)
movies_ratings = movies.merge(ratings, left_on='id', right_index=True)
# Simple merge
# movies_ratings = movies.merge(ratings, on='id', how='left')

# Print the first few rows of movies_ratings
print(movies_ratings.head())