# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv(r"Project_Investigate_Netflix_Movies\netflix_data.csv")

print(netflix_df.head())
# Start coding here! Use as many cells as you like
# netflix_df_movies = netflix_df[netflix_df['type'] == 'Movie']
# # print(netflix_df_movies)
# netflix_df_movies_90 = netflix_df_movies[(netflix_df_movies['release_year'] <= 1999) & (netflix_df_movies['release_year'] >= 1990)]
# # print(netflix_df_movies_90)
netflix_df_movies_90 = netflix_df[(netflix_df['type'] == 'Movie') & (netflix_df['release_year'] <= 1999) & (netflix_df['release_year'] >= 1990)]
# netflix_df_movies_90.groupby('duration')['duration'].sum()
# netflix_duration = netflix_df_movies_90.groupby('duration')['duration'].sum()
# netflix_duration.plot(kind='bar')
# netflix_df_movies_90['duration'].plot(kind='bar')
plt.hist(netflix_df_movies_90["duration"])
plt.show()

duration = 100

netflix_df_movies_90_action = netflix_df_movies_90[netflix_df_movies_90['genre'] == 'Action']
print(netflix_df_movies_90_action)

short_movie_count = 0
for lab, row in netflix_df_movies_90_action.iterrows():
    if row['duration'] < 90:
        short_movie_count += 1
print(short_movie_count)