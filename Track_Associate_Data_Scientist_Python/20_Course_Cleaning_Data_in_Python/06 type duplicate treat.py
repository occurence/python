import pandas as pd
import datetime as dt

ride_sharing = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\20_Course_Cleaning_Data_in_Python\datasets\ride_sharing_duplicate.csv')

# Drop complete duplicates from ride_sharing
ride_dup = ride_sharing.drop_duplicates(inplace=False)

# Create statistics dictionary for aggregation function
statistics = {'user_birth_year': 'min', 'duration': 'mean'}

# Group by ride_id and compute new statistics
ride_unique = ride_dup.groupby('ride_id').agg(statistics).reset_index()

# Find duplicated values again
duplicates = ride_unique.duplicated(subset = 'ride_id', keep = False)
duplicated_rides = ride_unique[duplicates == True]

# Assert duplicates are processed
assert duplicated_rides.shape[0] == 0

print(duplicated_rides[['ride_id','duration','user_birth_year']])