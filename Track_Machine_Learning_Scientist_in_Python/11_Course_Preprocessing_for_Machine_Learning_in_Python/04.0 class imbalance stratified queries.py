import pandas as pd

volunteer = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\11_Course_Preprocessing_for_Machine_Learning_in_Python\datasets\volunteer_opportunities.csv')

# print(volunteer.describe())
# print(volunteer.info())
# unq = volunteer.apply(lambda col: col.unique())
# unq = volunteer.apply(lambda col: col.nunique())
# unq = volunteer.apply(lambda col: col.nunique() if col.nunique() < 50 else None)
# unq = volunteer.apply(lambda col: col.nunique() if col.nunique() < 50 else None).dropna()
# unq = {col: volunteer[col].unique() for col in volunteer.select_dtypes(include=['object']).columns}
# print(unq)

# print(volunteer['category_desc'].unique().sum())
# print(volunteer['category_desc'].nunique())
# print(volunteer['category_desc'].values().nunique())
# print(volunteer['category_desc'].value_counts())
print(volunteer['category_desc'].value_counts() < 50)