import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_pickle(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\06_Course_Joining_Data_Pandas\datasets\movies.p')
movie_to_genres = pd.read_pickle(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\06_Course_Joining_Data_Pandas\datasets\movie_to_genres.p')
# pop = genres[genres['genre'].str.contains('Pop', case=False, na=False)]
# pop = genres[genres['genre'] == 'Pop']
pop_movies = movies.sort_values('popularity', ascending=False).head(10)
# print(pop)

# Use right join to merge the movie_to_genres and pop_movies tables
genres_movies = movie_to_genres.merge(pop_movies, how='right', 
                                      left_on='movie_id', 
                                      right_on='id')

# Count the number of genres
genre_count = genres_movies.groupby('genre').agg({'id':'count'})

# Plot a bar chart of the genre_count
genre_count.plot(kind='bar')
plt.show()
print(movie_to_genres.head())
print(pop_movies)