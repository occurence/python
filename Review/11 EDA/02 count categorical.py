import pandas as pd

unemployment = pd.read_csv(r'D:\STUDY\python\Review\11 EDA\datasets\clean_unemployment.csv')

# Count the values associated with each continent in unemployment
print(unemployment['continent'].value_counts())