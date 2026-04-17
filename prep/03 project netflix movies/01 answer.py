"""
Perform exploratory data analysis on the netflix_data.csv data to understand more about movies from the 1990s decade.
What was the most frequent movie duration in the 1990s? Save an approximate answer as an integer called duration (use 1990 as the decade's start year).
A movie is considered short if it is less than 90 minutes. Count the number of short action movies released in the 1990s and save this integer as short_movie_count.
Feel free to experiment after submitting the project!
"""

"""
Netflix! What started in 1997 as a DVD rental service has since exploded into one of the largest entertainment and media companies.
Given the large number of movies and series available on the platform, it is a perfect opportunity to flex your exploratory data analysis skills and dive into the entertainment industry.
You work for a production company that specializes in nostalgic styles. You want to do some research on movies released in the 1990's. You'll delve into Netflix data and perform exploratory data analysis to better understand this awesome movie decade!
You have been supplied with the dataset netflix_data.csv, along with the following table detailing the column names and descriptions. Feel free to experiment further after submitting!

The data
netflix_data.csv
Column	Description
show_id	The ID of the show
type	Type of show
title	Title of the show
director	Director of the show
cast	Cast of the show
country	Country of origin
date_added	Date added to Netflix
release_year	Year of Netflix release
duration	Duration of the show in minutes
description	Description of the show
genre	Show genre
"""

import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv(r"D:\STUDY\python\prep\03 project netflix movies\netflix_data.csv", index_col=0)

# Checking dataset
print(netflix_df.info())
print(netflix_df.isna().sum())
print(netflix_df['type'].value_counts())
print(netflix_df['country'].describe())
print(netflix_df['genre'].describe())
print(netflix_df.columns)

# What was the most frequent movie duration in the 1990s?
# Save an approximate answer as an integer called 
# duration (use 1990 as the decade's start year).
netflix_90s = netflix_df[(netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] < 2000)]
# print(netflix_90s.count())
# print(len(netflix_90s))
movies_90s = netflix_90s[netflix_90s['type'] == 'Movie']
# print(movies_90s.count())
print(len(movies_90s))

duration = movies_90s['duration'].mode().iloc[0]
print(f"""What was the most frequent movie duration in the 1990s?
Save an approximate answer as an integer called
duration (use 1990 as the decade's start year).\n{duration}""")
plt.hist(movies_90s['duration'])
plt.show()

# A movie is considered short if it is less than 90 minutes.
# Count the number of short action movies released in the
# 1990s and save this integer as short_movie_count.
short_action_movies = movies_90s[(movies_90s['genre'] == 'Action') & (movies_90s['duration'] < 90)]
short_movie_count = len(short_action_movies)
print(f"""A movie is considered short if it is less than 90 minutes.
Count the number of short action movies released in the 1990s
and save this integer as short_movie_count.\n{short_movie_count}""")