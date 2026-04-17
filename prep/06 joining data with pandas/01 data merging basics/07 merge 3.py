"""
Three table merge
To solidify the concept of a three DataFrame merge, practice another exercise. A reasonable extension of our review of Chicago business data would include looking at demographics information about the neighborhoods where the businesses are. A table with the median income by zip code has been provided to you. You will merge the licenses and wards tables with this new income-by-zip-code table called zip_demo.

The licenses, wards, and zip_demo DataFrames have been loaded for you.
"""

# Starting with the licenses table, merge to it the zip_demo table on the zip column. Then merge the resulting table to the wards table on the ward column. Save result of the three merged tables to a variable named licenses_zip_ward.
# Group the results of the three merged tables by the column alderman and find the median income.

import pandas as pd
licenses = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\licenses.csv')
zip_demo = pd.read_pickle(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\zip_demo.p')
wards = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\Chicago_wards.csv')

# Merge licenses and zip_demo, on zip; and merge the wards on ward
licenses_zip_ward = licenses.merge(zip_demo, on='zip') \
            			.merge(wards, on='ward')

# Print the results by alderman and show median income
print(licenses_zip_ward.groupby('alderman').agg({'income':'median'}))
# print(licenses_zip_ward.groupby('alderman')['income'].median())

# Nice work! 
# You successfully merged three tables together. 
# With the merged data, you can complete your income analysis. 
# You see that only a few aldermen represent businesses in areas where the median income is greater than $62,000, 
# which is the median income for the state of Illinois.