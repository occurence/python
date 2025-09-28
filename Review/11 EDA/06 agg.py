import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

books = pd.read_csv(r'D:\STUDY\python\Review\11 EDA\datasets\clean_books.csv')

print(books[['genre', 'rating', 'year']].groupby('genre').mean())
# Agg ungrouped data
print(books[['rating', 'year']].agg(['mean', 'std']))
# Agg grouped data
print(books[['genre', 'rating', 'year']].groupby('genre').agg(['mean', 'std']))
# Specifying different aggregations for different columns
print(books[['genre', 'rating', 'year']].groupby('genre').agg({'rating': 'mean', 'year': 'max'}))
# Specifying multiple aggregations for different columns
print(books.agg({'rating': ['mean', 'std'], 'year': 'median'}))
# Naming the output columns
print(books.groupby('genre').agg(
    mean_rating=('rating', 'mean'),
    std_rating=('rating', 'std'),
    median_year=('year', 'median')))

sns.barplot(data=books, x='genre', y='rating')
plt.show()