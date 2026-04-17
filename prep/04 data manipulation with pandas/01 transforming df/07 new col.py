"""
Adding new columns
You aren't stuck with just the data you are given. Instead, you can add new columns to a DataFrame. This has many names, such as transforming, mutating, and feature engineering.

You can create new columns from scratch, but it is also common to derive them from other columns, for example, by adding columns together or by changing their units.

homelessness is a DataFrame containing estimates of homelessness in each U.S. state in 2018. The individual column is the number of homeless individuals not part of a family with children. The family_members column is the number of homeless individuals part of a family with children. The state_pop column is the state's total population.

homelessness is available and pandas is loaded as pd.
"""

import pandas as pd
homelessness = pd.read_csv(r"D:\STUDY\python\prep\04 data manipulation with pandas\datasets\homelessness.csv", index_col=0)

# Add a new column to homelessness, named total, containing the sum of the individuals and family_members columns.
# Add another column to homelessness, named p_homeless, containing the proportion of the total homeless population to the total population in each state state_pop.

# Add total col as sum of individuals and family_members
homelessness['total'] = homelessness['individuals'] + homelessness['family_members']

# Add p_homeless col as proportion of total homeless population to the state population
homelessness['p_homeless'] = homelessness['total'] / homelessness['state_pop']

# See the result
print(homelessness)

# Astounding column assignment! 
# If your dataset doesn't have the exact columns you need, you can often make your own from what you have.