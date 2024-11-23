import pandas as pd

sequels = pd.read_pickle(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\06_Course_Joining_Data_Pandas\datasets\sequels.p')
financials = pd.read_pickle(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\06_Course_Joining_Data_Pandas\datasets\financials.p')

# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, on='id', how='left')

# Self merge with suffixes as inner join with left on sequel and right on id
orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel', 
                             right_on='id', right_index=True,
                             suffixes=('_org','_seq'))

# Add calculation to subtract revenue_org from revenue_seq 
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

# Select the title_org, title_seq, and diff 
titles_diff = orig_seq[['title_org','title_seq','diff']]

# Print the first rows of the sorted titles_diff
print(titles_diff.sort_values('diff', ascending=False).head())