import pandas as pd
import numpy as np
import re

ufo = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\11_Course_Preprocessing_for_Machine_Learning_in_Python\datasets\ufo_pattern.csv')
print(ufo[['length_of_time', 'state', 'type']].isna().sum())
ufo_no_missing = ufo.dropna(subset=['length_of_time', 'state', 'type'])
print(ufo_no_missing.shape)

def return_minutes(time_string):
    num = re.search('\d+', time_string)
    if num is not None:
        return int(num.group(0))
        
ufo["minutes"] = ufo["length_of_time"].apply(return_minutes)
print(ufo[['length_of_time','minutes']].head())

# Check the variance of the seconds and minutes columns
print(ufo[['seconds','minutes']].var())

# Log normalize the seconds column
ufo["seconds_log"] = np.log(ufo['seconds'])

# Print out the variance of just the seconds_log column
print(ufo['seconds_log'].var())