import pandas as pd

non_mus_tcks = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\06_Course_Joining_Data_Pandas\datasets\non_mus_tcks.csv')
top_invoices = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\06_Course_Joining_Data_Pandas\datasets\top_invoices.csv')
genres = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\06_Course_Joining_Data_Pandas\datasets\genres.csv')

# # Convert 'tid' columns to float64 to ensure compatibility for merging
non_mus_tcks['tid'] = pd.to_numeric(non_mus_tcks['tid'])
# top_invoices['tid'] = pd.to_numeric(top_invoices['tid'], errors='coerce')
# non_mus_tcks['tid'] = non_mus_tcks['tid'].astype(float)
# top_invoices['tid'] = top_invoices['tid'].astype(float)

# Merge the non_mus_tcks and top_invoices tables on tid
tracks_invoices = non_mus_tcks.merge(top_invoices, on='tid')

# Use .isin() to subset non_mus_tcks to rows with tid in tracks_invoices
top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]

# Group the top_tracks by gid and count the tid rows
cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid':'count'})

# Merge the genres table to cnt_by_gid on gid and print
print(cnt_by_gid.merge(genres, on='gid'))