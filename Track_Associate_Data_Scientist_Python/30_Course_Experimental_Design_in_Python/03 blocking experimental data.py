import pandas as pd

productivity_subjects = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\30_Course_Experimental_Design_in_Python\datasets\productivity_subjects.csv')

# Randomly assign half
block_1 = productivity_subjects.sample(n=50, random_state=42, replace=False)

# Set the block column
block_1['block'] = 1

# Create second assignment and label
block_2 = productivity_subjects.drop(block_1.index)
block_2['block'] = 2

# Concatenate and print
productivity_combined = pd.concat([block_1, block_2], axis=0)
print(productivity_combined['block'].value_counts())