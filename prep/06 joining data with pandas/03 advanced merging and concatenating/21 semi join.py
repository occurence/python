"""
Performing a semi join
Some of the tracks that have generated the most significant amount of revenue are from TV-shows or are other non-musical audio. You have been given a table of invoices that include top revenue-generating items. Additionally, you have a table of non-musical tracks from the streaming service. In this exercise, you'll use a semi join to find the top revenue-generating non-musical tracks.

The tables non_mus_tcks, top_invoices, and genres have been loaded for you.
"""

# Merge non_mus_tcks and top_invoices on tid using an inner join. Save the result as tracks_invoices.
# Use .isin() to subset the rows of non_mus_tcks where tid is in the tid column of tracks_invoices. Save the result as top_tracks.
# Group top_tracks by gid and count the tid rows. Save the result to cnt_by_gid.
# Merge cnt_by_gid with the genres table on gid and print the result.

import pandas as pd

non_mus_tcks = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\non_mus_tcks.csv')
top_invoices = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\top_invoices.csv')
genres = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\genres.csv')

# Merge the non_mus_tcks and top_invoices tables on tid
tracks_invoices = non_mus_tcks.merge(top_invoices, on='tid')

# Use .isin() to subset non_mus_tcks to rows with tid in tracks_invoices
top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]

# Group the top_tracks by gid and count the tid rows
cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid':'count'})
# cnt_by_gid = top_tracks.groupby(['gid'], as_index=False)['tid'].count()

# Merge the genres table to cnt_by_gid on gid and print
print(cnt_by_gid.merge(genres, on='gid'))

# Nice job! 
# In this exercise, you replicated a semi join to filter the table of tracks 
# by the table of invoice items to find the top revenue non-musical tracks. 
# With some additional data manipulation, 
# you discovered that _'TV-shows'_ is the non-musical genre that has the most top revenue-generating tracks. 
# Now that you've done both semi- and anti joins, it's time to move to the next topic.