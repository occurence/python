import pandas as pd

unemployment = pd.read_csv(r'D:\STUDY\python\Review\11 EDA\datasets\clean_unemployment.csv')

# Print the mean and standard deviation of rates for 2019 and 2020 
print(unemployment[["2019", "2020"]].agg(['mean', 'std']))

# Print mean and standard deviation grouped by continent
print(unemployment[["continent", "2019", "2020"]].groupby('continent').agg(['mean', 'std']))