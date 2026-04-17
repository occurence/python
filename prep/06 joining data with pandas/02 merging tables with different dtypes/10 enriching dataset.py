"""
Enriching a dataset
Setting how='left' with the .merge()method is a useful technique for enriching or enhancing a dataset with additional information from a different table. In this exercise, you will start off with a sample of movie data from the movie series Toy Story. Your goal is to enrich this data by adding the marketing tag line for each movie. You will compare the results of a left join versus an inner join.

The toy_story DataFrame contains the Toy Story movies. The toy_story and taglines DataFrames have been loaded for you.
"""

# Merge toy_story and taglines on the id column with a left join, and save the result as toystory_tag.
# With toy_story as the left table, merge to it taglines on the id column with an inner join, and save as toystory_tag.

import pandas as pd
toy_story = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\movies.csv')
toy_story = toy_story[toy_story['title'].str.contains('Toy Story')]
taglines = pd.read_pickle(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\taglines.p')

# Merge the toy_story and taglines tables with a left join
toystory_tag = toy_story.merge(taglines, on='id', how='left')

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)

# Merge the toy_story and taglines tables with a inner join
toystory_tag = toy_story.merge(taglines, on='id', how='inner')

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)

# That's fantastic work! 
# If your goal is to enhance or enrich a dataset, then you do not want to lose any of your original data. 
# A left join will do that by returning all of the rows of your left table, 
# while using an inner join may result in lost data if it does not exist in both tables.