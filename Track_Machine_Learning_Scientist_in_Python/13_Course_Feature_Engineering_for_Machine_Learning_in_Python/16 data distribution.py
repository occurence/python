import pandas as pd
import matplotlib.pyplot as plt

so_survey_df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\13_Course_Feature_Engineering_for_Machine_Learning_in_Python\datasets\Combined_DS_v10.csv')
so_survey_df['ConvertedSalary'] = so_survey_df['RawSalary'].str.replace(',', '').str.replace('$', '').str.replace('£', '').astype('float').fillna(0)
so_numeric_df = so_survey_df[['ConvertedSalary', 'Age', 'Years Experience']].copy()

# Create a histogram
so_numeric_df.hist()
plt.show()

# Create a boxplot of two columns
so_numeric_df[['Age', 'Years Experience']].boxplot()
plt.show()

# Create a boxplot of ConvertedSalary
so_numeric_df[['ConvertedSalary']].boxplot()
plt.show()

# Print summary statistics
print(so_numeric_df.describe())

print(so_numeric_df['ConvertedSalary'])