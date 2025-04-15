import pandas as pd

adult = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\16_Course_Working_with_Categorical_Data_in_Python\datasets\adult.csv')

# Group the adult dataset by "Sex" and "Above/Below 50k"
gb = adult.groupby(by=['Sex', 'Above/Below 50k'])

# Print out how many rows are in each created group
print(gb.size())

# Print out the mean of each group for all columns
# print(gb.mean())
print(gb[['Age','fnlgwt', 'Education Num', 'Capital Gain', 'Capital Loss', 'Hours/Week']].mean())