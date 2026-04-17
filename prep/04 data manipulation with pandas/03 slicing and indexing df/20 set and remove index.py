"""
Setting and removing indexes
pandas allows you to designate columns as an index. This enables cleaner code when taking subsets (as well as providing more efficient lookup under some circumstances).

In this chapter, you'll be exploring temperatures, a DataFrame of average temperatures in cities around the world. pandas is loaded as pd.
"""

# Look at temperatures.
# Set the index of temperatures to "city", assigning to temperatures_ind.
# Look at temperatures_ind. How is it different from temperatures?
# Reset the index of temperatures_ind, keeping its contents.
# Reset the index of temperatures_ind, dropping its contents.

import pandas as pd
temperatures = pd.read_csv(r"D:\STUDY\python\prep\04 data manipulation with pandas\datasets\temperatures.csv")

# Look at temperatures
print(temperatures)

# Set the index of temperatures to city
temperatures_ind = temperatures.set_index('city')

# Look at temperatures_ind
print(temperatures_ind)

# Reset the temperatures_ind index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the temperatures_ind index, dropping its contents
print(temperatures_ind.reset_index(drop=True))

# Incredible indexing! 
# Setting an index allows more concise code for subsetting for rows of a categorical variable via .loc[].