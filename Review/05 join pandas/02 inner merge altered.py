import pandas as pd

wards = pd.read_pickle(r'D:\STUDY\python\Review\05 join pandas\datasets\ward.p')
census = pd.read_pickle(r'D:\STUDY\python\Review\05 join pandas\datasets\census.p')

# Merge the wards and census tables on the ward column
wards_census = wards.merge(census, on='ward')

# Print the shape of wards_census
print('wards_census table shape:', wards_census.shape)

wards_altered = wards.copy()
wards_altered.loc[0,['ward']] = 61

# Print the first few rows of the wards_altered table to view the change 
print(wards_altered[['ward']].head())

# Merge the wards_altered and census tables on the ward column
wards_altered_census = wards_altered.merge(census, on='ward')

# Print the shape of wards_altered_census
print('wards_altered_census table shape:', wards_altered_census.shape)

census_altered = census.copy()
census_altered.loc[0,['ward']] = 'None'

# Print the first few rows of the census_altered table to view the change 
print(census_altered[['ward']].head())

# Merge the wards and census_altered tables on the ward column
wards_census_altered = wards.merge(census_altered, on='ward')

# Print the shape of wards_census_altered
print('wards_census_altered table shape:', wards_census_altered.shape)