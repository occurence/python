import pandas as pd

running_times_5k = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\11_Course_Preprocessing_for_Machine_Learning_in_Python\datasets\running_times_5k.csv')

# Use .loc to create a mean column
running_times_5k["mean"] = running_times_5k.loc[:, 'run1':'run5'].mean(axis=1)

# Take a look at the results
print(running_times_5k.head())