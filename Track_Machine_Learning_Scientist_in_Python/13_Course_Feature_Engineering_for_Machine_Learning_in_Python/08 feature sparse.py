import pandas as pd

so_survey_df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\13_Course_Feature_Engineering_for_Machine_Learning_in_Python\datasets\Combined_DS_v10.csv')
so_survey_df['ConvertedSalary'] = so_survey_df['ConvertedSalary'].fillna(0)

# Subset the DataFrame
sub_df = so_survey_df[['Age', 'Gender']]

# Print the number of non-missing values
print(sub_df.notnull().sum())