# Importing pandas and matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv(r"D:\STUDY\python\Review\03 investigating netflix movies\netflix_data.csv")
# print(netflix_df)
# print(netflix_df['type'].describe())
# print(netflix_df['genre'].describe())
# print(netflix_df['country'].describe())
# print(netflix_df['release_year'].describe())
# print(netflix_df.info())
# print(netflix_df.isna().sum())
# print(netflix_df['type'].value_counts())
# print(netflix_df.info())
# plt.plot(netflix_df['genre'])
# plt.show()

# plt.scatter(netflix_df['release_year'], netflix_df['duration'])
# plt.hist(netflix_df['duration'])
# plt.show()

netflix_df['in_90s'] = netflix_df['release_year'] >= 1990
netflix_df['is_short'] = netflix_df['duration'] < 90

print(netflix_df[['show_id','type','title','release_year','duration','genre','in_90s','is_short']].head(5))
# print(netflix_df.loc[[106],['show_id','type','title','release_year','duration','genre','in_90s','is_short']])

# netflix_df['duration']
in_90s = netflix_df[netflix_df['in_90s']][['show_id','type','title','release_year','duration','genre','is_short']]
print(in_90s['duration'].mode().iloc[0])
# print(in_90s['duration'].value_counts())

# # plt.hist(in_90s['duration'])
# # plt.show()

# print(np.logical_and(in_90s['genre'] == 'Action', in_90s['is_short'] == True))
print(in_90s[np.logical_and(in_90s['genre'] == 'Action', in_90s['is_short'] == True)])