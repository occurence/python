import pandas as pd

ride_sharing = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\20_Course_Cleaning_Data_in_Python\datasets\ride_sharing_duplicate.csv')

# Find duplicates
duplicates = ride_sharing.duplicated(subset=['ride_id'], keep=False)

# Sort your duplicated rides
duplicated_rides = ride_sharing[duplicates].sort_values('ride_id')

# Print relevant columns of duplicated_rides
print(duplicated_rides[['ride_id','duration','user_birth_year']])