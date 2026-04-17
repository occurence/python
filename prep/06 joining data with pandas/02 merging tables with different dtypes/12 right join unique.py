"""
Right join to find unique movies
Most of the recent big-budget science fiction movies can also be classified as action movies. You are given a table of science fiction movies called scifi_movies and another table of action movies called action_movies. Your goal is to find which movies are considered only science fiction movies. Once you have this table, you can merge the movies table in to see the movie names. Since this exercise is related to science fiction movies, use a right join as your superhero power to solve this problem.

The movies, scifi_movies, and action_movies tables have been loaded for you.
"""

# Merge action_movies and scifi_movies tables with a right join on movie_id. Save the result as action_scifi.
# Update the merge to add suffixes, where '_act' and '_sci' are suffixes for the left and right tables, respectively.
# From action_scifi, subset only the rows where the genre_act column is null.
# Merge movies and scifi_only using the id column in the left table and the movie_id column in the right table with an inner join.

import pandas as pd

movies = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\movies.csv', index_col=0)
genre = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\movie_to_genres.csv', index_col=0)
genre_movies = movies.merge(genre, left_on='id', right_on='movie_id', how='left')
scifi_movies = genre_movies[genre_movies['genre'] == 'Science Fiction'][['movie_id', 'genre']]
action_movies = genre_movies[genre_movies['genre'] == 'Action'][['movie_id', 'genre']]

# Merge action_movies to scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right')

# Merge action_movies to scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right',
                                   suffixes=('_act', '_sci'))

# Print the first few rows of action_scifi to see the structure
print(action_scifi.head())

# From action_scifi, select only the rows where the genre_act column is null
scifi_only = action_scifi[action_scifi['genre_act'].isnull()]

# Merge the movies and scifi_only tables with an inner join
movies_and_scifi_only = movies.merge(scifi_only, how='inner', left_on='id', right_on='movie_id')

# Print the first few rows and shape of movies_and_scifi_only
print(movies_and_scifi_only.head())
print(movies_and_scifi_only.shape)

# Well done, right join to the rescue! 
# You found over 250 action only movies by merging action_movies and scifi_movies using a right join. 
# With this, you were able to find the rows not found in the action_movies table. 
# Additionally, you used the left_on and right_on arguments to merge in the movies table. 
# Wow! You are a superhero.