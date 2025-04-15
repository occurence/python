import pandas as pd
homelessness = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\04_Course_Data_Manipulation_Pandas\homelessness.csv')

# Select the individuals column
individuals = homelessness['individuals']

print(individuals.head())

# Select the state and family_members columns
state_fam = homelessness[['state', 'family_members']]

print(state_fam.head())

# Select only the individuals and state columns, in that order
ind_state = homelessness[['individuals','state']]

print(ind_state.head())