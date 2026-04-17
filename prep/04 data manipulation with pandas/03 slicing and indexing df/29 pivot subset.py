"""
Subsetting pivot tables
A pivot table is just a DataFrame with sorted indexes, so the techniques you have learned already can be used to subset them. In particular, the .loc[] + slicing combination is often helpful.

pandas is loaded as pd. temp_by_country_city_vs_year is available.
"""

# Use .loc[] on temp_by_country_city_vs_year to take subsets.

# From Egypt to India.
# From Egypt, Cairo to India, Delhi.
# From Egypt, Cairo to India, Delhi, and 2005 to 2010.

import pandas as pd
temperatures = pd.read_csv(r"D:\STUDY\python\prep\04 data manipulation with pandas\datasets\temperatures.csv")
temperatures['year'] = pd.to_datetime(temperatures['date']).dt.year
temp_by_country_city_vs_year = temperatures.pivot_table('avg_temp_c', index=['country','city'], columns='year')

# Subset for Egypt to India
temp_by_country_city_vs_year.loc['Egypt':'India']
print(temp_by_country_city_vs_year.loc['Egypt':'India'])

# Subset for Egypt, Cairo to India, Delhi
temp_by_country_city_vs_year.loc[('Egypt','Cairo'):('India','Delhi')]
print(temp_by_country_city_vs_year.loc[('Egypt','Cairo'):('India','Delhi')])

# Subset for Egypt, Cairo to India, Delhi, and 2005 to 2010
temp_by_country_city_vs_year.loc[('Egypt','Cairo'):('India','Delhi'),'2005':'2010']
print(temp_by_country_city_vs_year.loc[('Egypt','Cairo'):('India','Delhi'),'2005':'2010'])

# Super pivot table subsetting! 
# Slicing is especially helpful for subsetting pivot tables.