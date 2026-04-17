import pandas as pd

so_survey_df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\13_Course_Feature_Engineering_for_Machine_Learning_in_Python\datasets\Combined_DS_v10.csv')

# Create a series out of the Country column
countries = so_survey_df['Country']

# Get the counts of each category
country_counts = countries.value_counts()
print(country_counts)
# Create a mask for only categories that occur less than 10 times
mask = countries.isin(country_counts[country_counts < 10].index)

# Label all other categories as Other
countries[mask] = 'Other'

# Print the updated category counts
print(so_survey_df['Country'].value_counts())