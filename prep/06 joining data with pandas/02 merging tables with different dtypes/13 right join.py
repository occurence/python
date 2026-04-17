"""
Popular genres with right join
What are the genres of the most popular movies? To answer this question, you need to merge data from the movies and movie_to_genres tables. In a table called pop_movies, the top 10 most popular movies in the movies table have been selected. To ensure that you are analyzing all of the popular movies, merge it with the movie_to_genres table using a right join. To complete your analysis, count the number of different genres. Also, the two tables can be merged by the movie ID. However, in pop_movies that column is called id, and in movie_to_genres it's called movie_id.

The pop_movies and movie_to_genres tables have been loaded for you.
"""

# Merge movie_to_genres and pop_movies using a right join. Save the results as genres_movies.
# Group genres_movies by genre and count the number of id values.

import pandas as pd
import matplotlib.pyplot as plt

movie_to_genres = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\movie_to_genres.csv')
movies = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\movies.csv')
pop_movies = movies.sort_values('popularity', ascending=False).head(10)

# Use right join to merge the movie_to_genres and pop_movies tables
genres_movies = movie_to_genres.merge(pop_movies, how='right', 
                                      left_on='movie_id', 
                                      right_on='id')

# Count the number of genres
genre_count = genres_movies.groupby('genre').agg({'id':'count'})
# genre_count = genres_movies.groupby('genre')['id'].count()

# Plot a bar chart of the genre_count
genre_count.plot(kind='bar')
plt.show()