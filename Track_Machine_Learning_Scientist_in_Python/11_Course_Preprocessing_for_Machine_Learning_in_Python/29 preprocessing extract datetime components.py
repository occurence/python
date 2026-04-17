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
print(ufo[['seconds','minutes']].var())
ufo["seconds_log"] = np.log(ufo['seconds'])
print(ufo['seconds_log'].var())

ufo["country_enc"] = ufo["country"].apply(lambda x: 1 if x == 'us' else 0)
print(len(ufo['type'].unique()))
type_set = pd.get_dummies(ufo['type'])
ufo = pd.concat([ufo, type_set], axis=1)

# Look at the first 5 rows of the date column
print(ufo['date'].head())

# Extract the month from the date column
ufo["month"] = pd.to_datetime(ufo["date"]).dt.month

# Extract the year from the date column
ufo["year"] = pd.to_datetime(ufo["date"]).dt.year

# Take a look at the head of all three columns
print(ufo[['date','month','year']].head())