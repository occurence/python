import pandas as pd

temperatures = pd.read_csv(r'D:\STUDY\python\Review\04 dataframe inspect\temperatures.csv')
temperatures_ind = temperatures.set_index(['city'])

# Make a list of cities to subset on
cities = ["London", "Paris"]

# Subset temperatures using square brackets
print(temperatures[temperatures['city'].isin(cities)])

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])