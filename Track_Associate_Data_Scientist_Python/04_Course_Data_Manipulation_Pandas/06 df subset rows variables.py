import pandas as pd
homelessness = pd.read_csv(r'D:\STUDY\python\Course_Data_Manipulation_Pandas\homelessness.csv')

# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness['state'].isin(canu)]

# See the result
print(mojave_homelessness)