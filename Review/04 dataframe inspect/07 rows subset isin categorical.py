import pandas as pd

homelessness = pd.read_csv(r'D:\STUDY\python\Review\04 dataframe inspect\homelessness.csv',index_col=0)

# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness['state'].isin(canu)]

# See the result
print(mojave_homelessness)