import pandas as pd

so_survey_df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\13_Course_Feature_Engineering_for_Machine_Learning_in_Python\datasets\Combined_DS_v10.csv')
so_survey_df['ConvertedSalary'] = so_survey_df['ConvertedSalary'].fillna(0)

# Import numpy
import numpy as np

# Specify the boundaries of the bins
bins = [-np.inf, 10000, 50000, 100000, 150000, np.inf]

# Bin labels
labels = ['Very low', 'Low', 'Medium', 'High', 'Very high']

# Bin the continuous variable ConvertedSalary using these boundaries
so_survey_df['boundary_binned'] = pd.cut(so_survey_df['ConvertedSalary'], 
                                         bins=bins, labels=labels)

# Print the first 5 rows of the boundary_binned column
print(so_survey_df[['boundary_binned', 'ConvertedSalary']].head())