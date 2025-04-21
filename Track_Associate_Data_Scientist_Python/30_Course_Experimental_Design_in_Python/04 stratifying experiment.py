import pandas as pd

wealth_data = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\30_Course_Experimental_Design_in_Python\datasets\wealth_data.csv')

# Create the first block
strata_1 = wealth_data[wealth_data['high_wealth'] == 1]
strata_1['Block'] = 1

# Create two groups assigning to Treatment or Control
strata_1_g1 = strata_1.sample(frac=0.5, replace=False)
strata_1_g1['T_C'] = 'T'
strata_1_g2 = strata_1.drop(strata_1_g1.index)
strata_1_g2['T_C'] = 'C'

# Create the second block and assign groups
strata_2 = wealth_data[wealth_data['high_wealth'] == 0]
strata_2['Block'] = 2

strata_2_g1 = strata_2.sample(900, replace=False)
strata_2_g1['T_C'] = 'T'
strata_2_g2 = strata_2.drop(strata_2_g1.index)
strata_2_g2['T_C'] = 'C'

# Concatenate the grouping work
wealth_data_stratified = pd.concat([strata_1_g1, strata_1_g2, strata_2_g1, strata_2_g2])
print(wealth_data_stratified.groupby(['Block','T_C', 'high_wealth']).size())