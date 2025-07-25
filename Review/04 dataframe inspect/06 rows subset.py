import pandas as pd

homelessness = pd.read_csv(r'D:\STUDY\python\Review\04 dataframe inspect\homelessness.csv',index_col=0)

# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness['individuals'] > 10000]

# See the result
print(ind_gt_10k)

# Filter for rows where region is Mountain
mountain_reg = homelessness[homelessness['region'] == 'Mountain']

# See the result
print(mountain_reg)

# Filter for rows where family_members is less than 1000 
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness['family_members'] < 1000) & (homelessness['region'] == 'Pacific')]

# See the result
print(fam_lt_1k_pac)