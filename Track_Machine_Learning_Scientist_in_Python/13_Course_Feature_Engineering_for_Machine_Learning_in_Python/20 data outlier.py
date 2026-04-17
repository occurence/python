import pandas as pd
import matplotlib.pyplot as plt

so_survey_df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\13_Course_Feature_Engineering_for_Machine_Learning_in_Python\datasets\Combined_DS_v10.csv')
so_survey_df['ConvertedSalary'] = so_survey_df['RawSalary'].str.replace(',', '').str.replace('$', '').str.replace('£', '').astype('float').fillna(0)
so_numeric_df = so_survey_df[['ConvertedSalary', 'Age', 'Years Experience']].copy()

# Find the 95th quantile
quantile = so_numeric_df['ConvertedSalary'].quantile(0.95)

# Trim the outliers
trimmed_df = so_numeric_df[so_numeric_df['ConvertedSalary'] < quantile]

# The original histogram
so_numeric_df[['ConvertedSalary']].hist()
plt.show()
# plt.clf()

# The trimmed histogram
trimmed_df[['ConvertedSalary']].hist()
plt.show()