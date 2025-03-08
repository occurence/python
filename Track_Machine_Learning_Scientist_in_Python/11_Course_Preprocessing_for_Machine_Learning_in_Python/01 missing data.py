import pandas as pd

volunteer = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\11_Course_Preprocessing_for_Machine_Learning_in_Python\datasets\volunteer_opportunities.csv')

print(volunteer['locality'].isna().sum())
print(volunteer.info())
print(volunteer.isna().sum())
print(volunteer.shape)