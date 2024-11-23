import pandas as pd

tracks_master = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\06_Course_Joining_Data_Pandas\datasets\tracks_master.csv')
tracks_ride = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\06_Course_Joining_Data_Pandas\datasets\tracks_ride.csv')
tracks_st = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\06_Course_Joining_Data_Pandas\datasets\tracks_st.csv')

# Concatenate the tracks
tracks_from_albums1 = pd.concat([tracks_master, tracks_ride, tracks_st],
                               sort=True)
print(tracks_from_albums1)

# Concatenate the tracks so the index goes from 0 to n-1
tracks_from_albums2 = pd.concat([tracks_master, tracks_ride, tracks_st],
                               ignore_index=True,
                               sort=True)
print(tracks_from_albums2)

# Concatenate the tracks, show only columns names that are in all tables
tracks_from_albums3 = pd.concat([tracks_master, tracks_ride, tracks_st],
                               join='inner',
                               sort=True)
print(tracks_from_albums3)