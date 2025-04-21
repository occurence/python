import pandas as pd

restaurants = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\20_Course_Cleaning_Data_in_Python\datasets\restaurant.csv')

# Inspect the unique values of the cuisine_type column
print(restaurants['cuisine_type'].unique())