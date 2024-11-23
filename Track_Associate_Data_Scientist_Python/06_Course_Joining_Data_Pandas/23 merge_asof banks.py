import pandas as pd
import matplotlib.pyplot as plt

jpm = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\06_Course_Joining_Data_Pandas\datasets\jpm.csv')
wells = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\06_Course_Joining_Data_Pandas\datasets\wells.csv')
bac = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\06_Course_Joining_Data_Pandas\datasets\bac.csv')

jpm['date_time'] = pd.to_datetime(jpm['date_time'])
wells['date_time'] = pd.to_datetime(wells['date_time'])
bac['date_time'] = pd.to_datetime(bac['date_time'])

# Use merge_asof() to merge jpm and wells
jpm_wells = pd.merge_asof(jpm, wells, on='date_time', direction='nearest', suffixes=('','_wells'))


# Use merge_asof() to merge jpm_wells and bac
jpm_wells_bac = pd.merge_asof(jpm_wells, bac, on='date_time', direction='nearest', suffixes=('_jpm', '_bac'))


# Compute price diff
price_diffs = jpm_wells_bac.diff()

# Plot the price diff of the close of jpm, wells and bac only
price_diffs.plot(y=['close_jpm', 'close_wells', 'close_bac'])
plt.show()