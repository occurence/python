import pandas as pd

unemployment = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\14_Course_Exploratory_Data_Analysis_in_Python\datasets\clean_unemployment.csv')

# Define a Series describing whether each continent is outside of Oceania
not_oceania = ~unemployment["continent"].isin(["Oceania"])

# Print unemployment without records related to countries in Oceania
print(unemployment[not_oceania])