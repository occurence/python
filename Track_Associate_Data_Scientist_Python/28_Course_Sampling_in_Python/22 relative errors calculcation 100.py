import pandas as pd

attrition_pop = pd.read_feather(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\28_Course_Sampling_in_Python\datasets\attrition.feather')

# Generate a simple random sample of 100 rows, with seed 2022
attrition_srs100 = attrition_pop.sample(n=100, random_state=2022)

# Calculate the mean employee attrition in the sample
mean_attrition_srs100 = attrition_srs100['Attrition'].mean()

# Calculate the relative error percentage
rel_error_pct100 = 100 * abs(attrition_pop['Attrition'].mean() - mean_attrition_srs100) / attrition_pop['Attrition'].mean()

# Print rel_error_pct100
print(rel_error_pct100)