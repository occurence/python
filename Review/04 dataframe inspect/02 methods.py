import pandas as pd

homelessness = pd.read_csv(r'D:\STUDY\python\Review\04 dataframe inspect\homelessness.csv',index_col=0)

# Print the head of the homelessness data
print(homelessness.head())

# Print information about homelessness
print(homelessness.info())

# Print the shape of homelessness
print(homelessness.shape)

# Print a description of homelessness
print(homelessness.describe())