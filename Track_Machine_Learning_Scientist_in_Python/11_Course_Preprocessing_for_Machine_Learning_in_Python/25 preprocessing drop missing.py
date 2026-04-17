import pandas as pd

ufo = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\11_Course_Preprocessing_for_Machine_Learning_in_Python\datasets\ufo_sightings_large.csv')
ufo = ufo[['date', 'length_of_time', 'state', 'type']]

# Count the missing values in the length_of_time, state, and type columns, in that order
print(ufo[['length_of_time', 'state', 'type']].isna().sum())

# Drop rows where length_of_time, state, or type are missing
ufo_no_missing = ufo.dropna(subset=['length_of_time', 'state', 'type'])

# Print out the shape of the new dataset
print(ufo_no_missing.shape)