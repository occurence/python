"""
Concatenation basics
You have been given a few tables of data with musical track info for different albums from the metal band, Metallica. 
The track info comes from their Ride The Lightning, Master Of Puppets, and St. Anger albums. 
Try various features of the .concat() method by concatenating the tables vertically together in different ways.

The tables tracks_master, tracks_ride, and tracks_st have loaded for you.
"""

# Concatenate tracks_master, tracks_ride, and tracks_st, in that order, setting sort to True.
# Concatenate tracks_master, tracks_ride, and tracks_st, where the index goes from 0 to n-1.
# Concatenate tracks_master, tracks_ride, and tracks_st, showing only columns that are in all tables.

import pandas as pd

tracks_master = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\tracks_master.csv', index_col=0)
tracks_ride = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\tracks_ride.csv', index_col=0)
tracks_st = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\tracks_st.csv', index_col=0)

print(tracks_master)

# Concatenate the tracks
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               sort=True)
print(tracks_from_albums)

# Concatenate the tracks so the index goes from 0 to n-1
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               ignore_index=True,
                               sort=True)
print(tracks_from_albums)

# Concatenate the tracks, show only columns names that are in all tables
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               join='inner',
                               sort=True)
print(tracks_from_albums)

# Great job! 
# You've concatenated your first set of tables, adjusted the index, and altered the columns shown in the output. 
# The .concat() method is a very flexible tool that is useful for combining data into a new dataset.

print(pd.concat([tracks_master, tracks_ride, tracks_st],
                               ignore_index=True,
                               join='inner',
                               sort=True))