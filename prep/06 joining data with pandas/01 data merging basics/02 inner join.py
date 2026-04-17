"""
Your first inner join
You have been tasked with figuring out what the most popular types of fuel used in Chicago taxis are. To complete the analysis, you need to merge the taxi_owners and taxi_veh tables together on the vid column. You can then use the merged table along with the .value_counts() method to find the most common fuel_type.

Since you'll be working with pandas throughout the course, the package will be preloaded for you as pd in each exercise in this course. Also the taxi_owners and taxi_veh DataFrames are loaded for you.
"""

# Merge taxi_owners with taxi_veh on the column vid, and save the result to taxi_own_veh.
# Set the left and right table suffixes for overlapping columns of the merge to _own and _veh, respectively.
# Select the fuel_type column from taxi_own_veh and print the value_counts() to find the most popular fuel_types used.

import pandas as pd
taxi_owners = pd.read_csv(r"D:\STUDY\python\prep\06 joining data with pandas\datasets\taxi_owners.csv", index_col=0)
taxi_veh = pd.read_csv(r"D:\STUDY\python\prep\06 joining data with pandas\datasets\taxi_vehicles.csv", index_col=0)

# Merge the taxi_owners and taxi_veh tables
# taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid')

# Merge the taxi_owners and taxi_veh tables setting a suffix
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own','_veh'))

# Print the column names of the taxi_own_veh
print(taxi_own_veh.columns)

# Print the value_counts to find the most popular fuel_type
print(taxi_own_veh['fuel_type'].value_counts())

# Bravo! 
# You correctly merged the two tables together and 
# found out that the most common fuel type for taxis in Chicago are hybrids.