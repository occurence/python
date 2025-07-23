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
homelessness['total'] = homelessness['individuals'] + homelessness['family_members']
homelessness['p_homeless'] = homelessness['total'] / homelessness['state_pop']
print(homelessness.head())

# Sort Rows, Subset Cols, Subset Rows, New Cols
homelessness["indiv_per_10k"] = 10000 * homelessness['individuals'] / homelessness['state_pop'] 
high_homelessness = homelessness[homelessness['indiv_per_10k'] > 20]
high_homelessness_srt = high_homelessness.sort_values('indiv_per_10k', ascending=False)
result = high_homelessness_srt[['state','indiv_per_10k']]
print(result)

# Summary Statistics
print(homelessness['state_pop'].mean())
print(homelessness['state_pop'].median())
# Aggregate Functions
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
print(homelessness[["individuals", "family_members", "state_pop"]].agg([iqr,'median']))

# Cumulative Statistics
homelessness_atlantic = homelessness[(homelessness['region'] == 'South Atlantic') | (homelessness['region'] == 'Mid-Atlantic')]
homelessness_atlantic = homelessness_atlantic.sort_values('state_pop', ascending=True)
homelessness_atlantic['cum_state_pop'] = homelessness_atlantic['state_pop'].cumsum()
homelessness_atlantic['cum_max_state_pop'] = homelessness_atlantic['state_pop'].cummax()
print(homelessness_atlantic[["region","state","state_pop", "cum_state_pop", "cum_max_state_pop"]])

# Count, Remove Duplicates and Categorical
unique_locs = homelessness.drop_duplicates(subset=['region','state'])
print(unique_locs)
print(unique_locs['region'].value_counts(sort=True))
print(unique_locs['region'].value_counts(normalize=True))