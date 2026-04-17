"""
Self join
Merging a table to itself can be useful when you want to compare values in a column to other values in the same column. In this exercise, you will practice this by creating a table that for each movie will list the movie director and a member of the crew on one row. You have been given a table called crews, which has columns id, job, and name. First, merge the table to itself using the movie ID. This merge will give you a larger table where for each movie, every job is matched against each other. Then select only those rows with a director in the left table, and avoid having a row where the director's job is listed in both the left and right tables. This filtering will remove job combinations that aren't with the director.

The crews table has been loaded for you.
"""

# To a variable called crews_self_merged, merge the crews table to itself on the id column using an inner join, setting the suffixes to '_dir' and '_crew' for the left and right tables respectively.
# Create a Boolean index, named boolean_filter, that selects rows from the left table with the job of 'Director' and avoids rows with the job of 'Director' in the right table.
# Use the .head() method to print the first few rows of direct_crews.

import pandas as pd

crews = pd.read_pickle(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\crews.p')
print(crews.head())

# Merge the crews table to itself
crews_self_merged = crews.merge(crews, on='id', suffixes=('_dir','_crew'))

# Create a Boolean index to select the appropriate
boolean_filter = ((crews_self_merged['job_dir'] == 'Director') & 
     (crews_self_merged['job_crew'] != 'Director'))
direct_crews = crews_self_merged[boolean_filter]

# Print the first few rows of direct_crews
print(direct_crews.head())

# Great job! 
# By merging the table to itself, 
# you compared the value of the __director__ from the jobs column to other values from the jobs column. 
# With the output, you can quickly see different movie directors and the people they worked with in the same movie.