import pandas as pd

unemployment = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\14_Course_Exploratory_Data_Analysis_in_Python\datasets\clean_unemployment.csv')

# Print the mean and standard deviation of rates by year
# print(unemployment.agg(['mean','std']))
print(unemployment[['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']].agg(['mean','std']))

# Print yearly mean and standard deviation grouped by continent
# print(unemployment.groupby('continent').agg(['mean','std']))
print(unemployment.groupby('continent')[['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']].agg(['mean','std']))