import pandas as pd

homelessness = pd.read_csv(r'D:\STUDY\python\Review\04 dataframe inspect\homelessness.csv')

# Methods
print(homelessness.head())
print(homelessness.info())
print(homelessness.describe())
print(homelessness.isna().sum())
print(homelessness['state'].value_counts().head(5))

# Attributes
print(homelessness.values)
print(homelessness.columns)
print(homelessness.index)
print(homelessness.shape)

print(homelessness.head(5))

# Sort Rows
print(homelessness.sort_values('family_members', ascending=False).head(5))
# Subset Cols
print(homelessness[['state','family_members']])
# Subset Rows
print(homelessness[(homelessness['family_members'] < 1000) & (homelessness['region'] == 'Pacific')])
# Subset Rows isin Categorical Variables
canu = ["California", "Arizona", "Nevada", "Utah"]
print(homelessness[homelessness['state'].isin(canu)])

# Add/Mutate/Transform/Feature Engineering/convert
