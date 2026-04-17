import pandas as pd

so_survey_df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\13_Course_Feature_Engineering_for_Machine_Learning_in_Python\datasets\Combined_DS_v10.csv')

# Create dummy variables for the Country column
dummy = pd.get_dummies(so_survey_df, columns=['Country'], drop_first=True, prefix='DM')

# Print the columns names
print(dummy.columns)