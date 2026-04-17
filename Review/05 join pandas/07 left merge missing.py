import pandas as pd

movies = pd.read_pickle(r'D:\STUDY\python\Review\05 join pandas\datasets\movies.p')
financials = pd.read_pickle(r'D:\STUDY\python\Review\05 join pandas\datasets\financials.p')

# Merge the movies table with the financials table with a left join
movies_financials = movies.merge(financials, on='id', how='left')

# Count the number of rows in the budget column that are missing
number_of_missing_fin = movies_financials['budget'].isna().sum()

# Print the number of movies missing financials
print(number_of_missing_fin)