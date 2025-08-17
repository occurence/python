import pandas as pd

movies = pd.read_pickle(r'D:\STUDY\python\Review\05 join pandas\datasets\movies.p')
casts = pd.read_pickle(r'D:\STUDY\python\Review\05 join pandas\datasets\casts.p')

print(movies[movies['title'].isin(['Iron Man', 'Iron Man 2'])])

iron_1_movie = movies.loc[movies['title'].isin(['Iron Man']), 'id'].iloc[0]
iron_1_actors = casts.loc[casts['movie_id'] == iron_1_movie][['character', 'id', 'name']]

iron_2_movie = movies.loc[movies['title'].isin(['Iron Man 2']), 'id'].iloc[0]
iron_2_actors = casts.loc[casts['movie_id'] == iron_2_movie][['character', 'id', 'name']]

# Merge iron_1_actors to iron_2_actors on id with outer join using suffixes
iron_1_and_2 = iron_1_actors.merge(iron_2_actors,
                                     how='outer',
                                     on='id',
                                     suffixes=('_1','_2'))

# Create an index that returns true if name_1 or name_2 are null
m = ((iron_1_and_2['name_1'].isnull()) | 
     (iron_1_and_2['name_2'].isnull()))

# Print the first few rows of iron_1_and_2
print(iron_1_and_2[m].head())