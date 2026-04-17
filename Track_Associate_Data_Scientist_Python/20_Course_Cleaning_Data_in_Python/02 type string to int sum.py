import pandas as pd

ride_sharing = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\20_Course_Cleaning_Data_in_Python\datasets\ride_sharing_new.csv')

# Strip duration of minutes
ride_sharing['duration_trim'] = ride_sharing['duration'].str.strip('minutes')

# Convert duration to integer
ride_sharing['duration_time'] = ride_sharing['duration_trim'].astype('int')

# Write an assert statement making sure of conversion
assert ride_sharing['duration_time'].dtype == 'int'

# Print formed columns and calculate average ride duration 
print(ride_sharing[['duration','duration_trim','duration_time']])
print(ride_sharing['duration_time'].mean())