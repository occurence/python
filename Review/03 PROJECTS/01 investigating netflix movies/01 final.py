# Importing pandas and matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv(r"D:\STUDY\python\Review\03 investigating netflix movies\netflix_data.csv")

# Checking dataset
print(netflix_df.info())
print(netflix_df.isna().sum())
print(netflix_df['type'].value_counts())
print(netflix_df['country'].describe())
print(netflix_df['genre'].describe())

features = ['show_id','type','title','release_year','duration','genre']
netflix_90s = netflix_df[(netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] < 2000)]
# print(netflix_90s[features])
movies_90s = netflix_90s[netflix_90s['type'] == 'Movie']
# print(movies_90s)
duration = movies_90s['duration'].mode().iloc[0]
print(f"What was the most frequent movie duration in the 1990s? Save an approximate answer as an integer called duration (use 1990 as the decade's start year).\n{duration}")
plt.hist(movies_90s['duration'])
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.show()

short_action_movies = movies_90s[(movies_90s['genre'] == 'Action') & (movies_90s['duration'] < 90)]
# short_movie_count = short_action_movies.count(axis=0)
# short_movie_count = short_action_movies.shape[0]
short_movie_count = len(short_action_movies)
print(f"A movie is considered short if it is less than 90 minutes. Count the number of short action movies released in the 1990s and save this integer as short_movie_count.\n{short_movie_count}")