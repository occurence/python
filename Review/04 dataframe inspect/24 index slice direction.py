import pandas as pd

temperatures = pd.read_csv(r'D:\STUDY\python\Review\04 dataframe inspect\temperatures.csv')

# Index temperatures by country & city
temperatures_ind = temperatures.set_index(['country','city'])

# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[('India','Hyderabad'):('Iraq','Baghdad')])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:, 'date':'avg_temp_c'])

# Subset in both directions at once
print(temperatures_srt.loc[('India','Hyderabad'):('Iraq','Baghdad'), 'date':'avg_temp_c'])