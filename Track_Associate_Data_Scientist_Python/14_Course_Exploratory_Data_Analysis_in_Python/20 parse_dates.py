import pandas as pd

# Import divorce.csv, parsing the appropriate columns as dates in the import
divorce = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\14_Course_Exploratory_Data_Analysis_in_Python\datasets\divorce.csv', parse_dates=['divorce_date','dob_man','dob_woman','marriage_date'])
print(divorce.dtypes)