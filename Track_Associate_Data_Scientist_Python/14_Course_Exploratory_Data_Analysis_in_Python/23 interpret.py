import pandas as pd

divorce = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\14_Course_Exploratory_Data_Analysis_in_Python\datasets\divorce.csv', parse_dates=['marriage_date'])

"""Possible answers
marriage_duration is strongly positively correlated with marriage_month.
The correlation between num_kids and income_man is stronger than the correlation between num_kids and marriage_duration.
A later marriage_year causes a lower number of children, represented by num_kids.
A later marriage_year is correlated with having fewer children."""

# divorce['marriage_duration'].corr(divorce['marriage_month'])
print(divorce['marriage_duration'].corr(divorce['marriage_date'].dt.month))
print(divorce['num_kids'].corr(divorce['income_man']))
print(divorce['num_kids'].corr(divorce['marriage_duration']))
# divorce['marriage_year'].corr(divorce['num_kids'])
print(divorce['marriage_date'].dt.year.corr(divorce['num_kids']))