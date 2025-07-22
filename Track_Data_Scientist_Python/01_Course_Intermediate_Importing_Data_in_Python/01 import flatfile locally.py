# Import package
from urllib.request import urlretrieve

# Import pandas
import pandas as pd

# Assign url of file: url
url = 'https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Save file locally
urlretrieve(url, 'D:/STUDY/python/Track_Data_Scientist_Python/01_Course_Intermediate_Importing_Data_in_Python/datasets/winequality-red.csv')

# Read file into a DataFrame and print its head
df = pd.read_csv(r'D:\STUDY\python\Track_Data_Scientist_Python\01_Course_Intermediate_Importing_Data_in_Python\datasets\winequality-red.csv', sep=';')
print(df.head())