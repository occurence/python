import pandas as pd

taxi_owners = pd.read_pickle(r'D:\STUDY\python\Review\05 join pandas\taxi_owners.p')
taxi_veh = pd.read_pickle(r'D:\STUDY\python\Review\05 join pandas\taxi_vehicles.p')

# Merge the taxi_owners and taxi_veh tables setting a suffix
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own','_veh'))

# Print the column names of the taxi_own_veh
print(taxi_own_veh.columns)

# Print the value_counts to find the most popular fuel_type
print(taxi_own_veh['fuel_type'].value_counts())