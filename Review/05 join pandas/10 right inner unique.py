import pandas as pd

movies = pd.read_pickle(r'D:\STUDY\python\Review\05 join pandas\datasets\movies.p')
genres = pd.read_pickle(r'D:\STUDY\python\Review\05 join pandas\datasets\movie_to_genres.p')
scifi_movies = genres[genres['genre'] == 'Science Fiction']
action_movies = genres[genres['genre'] == 'Action']

# Merge action_movies to the scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right',
                                   suffixes=('_act','_sci'))

# From action_scifi, select only the rows where the genre_act column is null
scifi_only = action_scifi[action_scifi['genre_act'].isnull()]

# Merge the movies and scifi_only tables with an inner join
movies_and_scifi_only = movies.merge(scifi_only, how='inner', left_on='id', right_on='movie_id')

# Print the first few rows and shape of movies_and_scifi_only
print(movies_and_scifi_only.head())
print(movies_and_scifi_only.shape)