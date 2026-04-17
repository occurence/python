import pandas as pd
from thefuzz import process

restaurants = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\20_Course_Cleaning_Data_in_Python\datasets\restaurant.csv')

# Create a list of matches, comparing 'italian' with the cuisine_type column
matches = process.extract('italian', restaurants['cuisine_type'], limit=len(restaurants['cuisine_type']))

# Inspect the first 5 matches
print(matches[0:5])