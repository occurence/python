import pandas as pd
homelessness = pd.read_csv(r'D:\STUDY\python\Course_Data_Manipulation_Pandas\homelessness.csv')


# Add total col as sum of individuals and family_members
homelessness['total'] = homelessness['individuals'] + homelessness['family_members']

# Add p_homeless col as proportion of total homeless population to the state population
homelessness['p_homeless'] = homelessness['total']/homelessness['state_pop']

# See the result
print(homelessness)