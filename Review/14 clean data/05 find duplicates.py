import pandas as pd

ride_sharing = pd.read_csv(r'D:\STUDY\python\Review\14 clean data\datasets\ride_sharing_duplicate.csv')

print(ride_sharing.info())
# print(ride_sharing.index)

# Find duplicates
duplicates = ride_sharing.duplicated(subset=['ride_id'], keep=False)

# Sort your duplicated rides
duplicated_rides = ride_sharing[duplicates].sort_values('ride_id')

# Print relevant columns of duplicated_rides
print(duplicated_rides[['ride_id','duration','user_birth_year']])