"""
Subsetting rows by categorical variables
Subsetting data based on a categorical variable often involves using the or operator (|) to select rows from multiple categories. This can get tedious when you want all states in one of three different regions, for example. Instead, use the .isin() method, which will allow you to tackle this problem by writing one condition instead of three separate ones.

colors = ["brown", "black", "tan"]
condition = dogs["color"].isin(colors)
dogs[condition]
homelessness is available and pandas is loaded as pd.
"""

# Filter homelessness for cases where the USA census state is in the list of Mojave states, canu, assigning to mojave_homelessness. View the printed result.

import pandas as pd
homelessness = pd.read_csv(r"D:\STUDY\python\prep\04 data manipulation with pandas\datasets\homelessness.csv", index_col=0)

# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness['state'].isin(canu)]

# See the result
print(mojave_homelessness)

# Success _is in_ the air! Using .isin() makes subsetting categorical variables a breeze.