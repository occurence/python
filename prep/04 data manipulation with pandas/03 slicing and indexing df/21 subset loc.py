"""
Subsetting with .loc[]
The killer feature for indexes is .loc[]: a subsetting method that accepts index values. When you pass it a single argument, it will take a subset of rows.

The code for subsetting using .loc[] can be easier to read than standard square bracket subsetting, which can make your code less burdensome to maintain.

pandas is loaded as pd. temperatures and temperatures_ind are available; the latter is indexed by city.
"""

# Create a list called cities that contains "London" and "Paris".
# Use [] subsetting to filter temperatures for rows where the city column takes a value in the cities list.
# Use .loc[] subsetting to filter temperatures_ind for rows where the city is in the cities list.

import pandas as pd
temperatures = pd.read_csv(r"D:\STUDY\python\prep\04 data manipulation with pandas\datasets\temperatures.csv")
temperatures_ind = temperatures.set_index('city')

# Make a list of cities to subset on
cities = ["London", "Paris"]

# Subset temperatures using square brackets
print(temperatures[temperatures['city'].isin(cities)])

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])

# .loc[] is used by all the best folk! 
# Setting an index allows more concise code for subsetting rows via .loc[].

print(temperatures_ind.loc['London':'Paris']) # contains unnecessary rows between London and Paris