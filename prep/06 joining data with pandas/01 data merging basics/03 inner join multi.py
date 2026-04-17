"""
Inner joins and number of rows returned
All of the merges you have studied to this point are called inner joins. It is necessary to understand that inner joins only return the rows with matching values in both tables. You will explore this further by reviewing the merge between the wards and census tables, then comparing it to merges of copies of these tables that are slightly altered, named wards_altered, and census_altered. The first row of the wards column has been changed in the altered tables. You will examine how this affects the merge between them. The tables have been loaded for you.

For this exercise, it is important to know that the wards and census tables start with 50 rows.
"""

import pandas as pd
wards = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\Chicago_wards.csv', index_col=0)
census = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\Chicago_census.csv', index_col=0)

wards_altered = wards.copy()
census_altered = census.copy()
wards.loc[0,['ward']] = 1
census.loc[0,['ward']] = 1

# Merge wards and census on the ward column and save the result to wards_census.
# Merge the wards and census tables on the ward column
wards_census = wards.merge(census, on='ward')

# Print the shape of wards_census
print('wards_census table shape:', wards_census.shape)

###########################################
###########################################
###########################################
# Merge the wards_altered and census tables on the ward column, and notice the difference in returned rows.
# Print the first few rows of the wards_altered table to view the change 
print(wards_altered[['ward']].head())

# Merge the wards_altered and census tables on the ward column
wards_altered_census = wards_altered.merge(census, on='ward')

# Print the shape of wards_altered_census
print('wards_altered_census table shape:', wards_altered_census.shape)

###########################################
###########################################
###########################################
# Merge the wards and census_altered tables on the ward column, and notice the difference in returned rows.
# Print the first few rows of the census_altered table to view the change 
print(census_altered[['ward']].head())

# Merge the wards and census_altered tables on the ward column
wards_census_altered = wards.merge(census_altered, on='ward')

# Print the shape of wards_census_altered
print('wards_census_altered table shape:', wards_census_altered.shape)

# Great job! 
# In step 1, the .merge() returned a table with the same number of rows as the original wards table. 
# However, in steps 2 and 3, using the altered tables with the altered first row of the ward column, 
# the number of returned rows was fewer. There was not a matching value in the ward column of the other table. 
# _Remember that .merge() only returns rows where the values match in both tables._