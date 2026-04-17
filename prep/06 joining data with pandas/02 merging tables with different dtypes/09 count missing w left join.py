"""
Counting missing rows with left join
The Movie Database is supported by volunteers going out into the world, collecting data, and entering it into the database. This includes financial data, such as movie budget and revenue. If you wanted to know which movies are still missing data, you could use a left join to identify them. Practice using a left join by merging the movies table and the financials table.

The movies and financials tables have been loaded for you.
"""

import pandas as pd
movies = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\movies.csv')
financials = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\financials.csv')

# What column is likely the best column to merge the two tables on?

# Possible answers

# on='budget'
# on='popularity'
# on='id' # Correct

# Merge the movies table, as the left table, with the financials table using a left join, and save the result to movies_financials.
# Count the number of rows in movies_financials with a null value in the budget column.

# Merge movies and financials with a left join
movies_financials = movies.merge(financials, on='id', how='left')

# Merge the movies table with the financials table with a left join
movies_financials = movies.merge(financials, on='id', how='left')

# Count the number of rows in the budget column that are missing
number_of_missing_fin = movies_financials['budget'].isna().sum()

# Print the number of movies missing financials
print(number_of_missing_fin)

# Great job! 
# You used a left join to find out which rows in the financials table were missing data. 
# When performing a left join, the .merge() method returns a row full of null values for columns in the right table 
# if the key column does not have a matching value in both tables. 
# We see that there are at least 1,500 rows missing data. Wow! That sounds like a lot of work.