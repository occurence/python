import pandas as pd

tracks_master = pd.read_csv(r'D:\STUDY\python\Review\05 join pandas\datasets\tracks_master.csv', index_col=0)
tracks_ride = pd.read_csv(r'D:\STUDY\python\Review\05 join pandas\datasets\tracks_ride.csv', index_col=0)
tracks_st = pd.read_csv(r'D:\STUDY\python\Review\05 join pandas\datasets\tracks_st.csv', index_col=0)

# Concatenate the tracks so the index goes from 0 to n-1
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                            #    ignore_index=True,
                               join='inner',
                               sort=True)
print(tracks_from_albums)