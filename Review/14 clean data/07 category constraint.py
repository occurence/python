import pandas as pd

airlines = pd.read_csv(r'D:\STUDY\python\Review\14 clean data\datasets\airlines_final.csv', index_col=0)
categories = pd.read_csv(r'D:\STUDY\python\Review\14 clean data\datasets\airlines_categories.csv')

print(airlines.head)
print(categories.head)

# Find the cleanliness category in airlines not in categories
cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])

# Find rows with that category
cat_clean_rows = airlines['cleanliness'].isin(cat_clean)

# Print rows with inconsistent category
print(airlines[cat_clean_rows])

# Print rows with consistent categories only
print(airlines[~cat_clean_rows])