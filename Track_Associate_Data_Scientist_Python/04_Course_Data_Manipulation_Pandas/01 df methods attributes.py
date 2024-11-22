import pandas as pd
homelessness = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\04_Course_Data_Manipulation_Pandas\homelessness.csv')


# Print the head of the homelessness data
print(homelessness.head())

# Print information about homelessness
print(homelessness.info())

# Print the shape of homelessness
print(homelessness.shape)

# Print a description of homelessness
print(homelessness.describe())