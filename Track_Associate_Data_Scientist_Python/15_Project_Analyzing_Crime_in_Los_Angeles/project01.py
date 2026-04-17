import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

crimes = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\15_Project_Analyzing_Crime_in_Los_Angeles\crimes.csv', parse_dates=['Date Rptd', 'DATE OCC'], dtype={'TIME OCC': str})
crimes.head()

# Start coding here
# Use as many cells as you need

# Which hour has the highest frequency of crimes? Store as an integer variable called peak_crime_hour.
# print(crimes.groupby('TIME OCC')['TIME OCC'].value_counts())
time_category = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
time_conditions = [
    (crimes['TIME OCC'].str.contains('^00')),
    (crimes['TIME OCC'].str.contains('^01')),
    (crimes['TIME OCC'].str.contains('^02')),
    (crimes['TIME OCC'].str.contains('^03')),
    (crimes['TIME OCC'].str.contains('^04')),
    (crimes['TIME OCC'].str.contains('^05')),
    (crimes['TIME OCC'].str.contains('^06')),
    (crimes['TIME OCC'].str.contains('^07')),
    (crimes['TIME OCC'].str.contains('^08')),
    (crimes['TIME OCC'].str.contains('^09')),
    (crimes['TIME OCC'].str.contains('^10')),
    (crimes['TIME OCC'].str.contains('^11')),
    (crimes['TIME OCC'].str.contains('^12')),
    (crimes['TIME OCC'].str.contains('^13')),
    (crimes['TIME OCC'].str.contains('^14')),
    (crimes['TIME OCC'].str.contains('^15')),
    (crimes['TIME OCC'].str.contains('^16')),
    (crimes['TIME OCC'].str.contains('^17')),
    (crimes['TIME OCC'].str.contains('^18')),
    (crimes['TIME OCC'].str.contains('^19')),
    (crimes['TIME OCC'].str.contains('^20')),
    (crimes['TIME OCC'].str.contains('^21')),
    (crimes['TIME OCC'].str.contains('^22')),
    (crimes['TIME OCC'].str.contains('^23'))
]

crimes['time_category'] = np.select(time_conditions, time_category, default='xx')
print(crimes.groupby(['time_category'])['time_category'].count())
# print(crimes.groupby(['time_category'])['time_category'].count().head())
# print(crimes['time_category'].value_counts(sort=True).head(1).index[0])
peak_crime_hour = crimes['time_category'].value_counts(sort=True).index[0]
print(f'The hour with the highest frequency of crimes: {peak_crime_hour}')


# Which area has the largest frequency of night crimes (crimes committed between 10pm and 3:59am)?
# Save as a string variable called peak_night_crime_location.
# print(crimes['AREA NAME'].value_counts(dropna=False, sort=True))
# print(crimes['time_category'].isin(['10','11','00','01','02','03']))
night_crimes = crimes[crimes['time_category'].isin(['22','23','00','01','02','03'])]
# print(night_crimes.groupby(['AREA NAME'])['AREA NAME'].count())
# print(night_crimes['AREA NAME'].value_counts(sort=True))
peak_night_crime_location = night_crimes['AREA NAME'].value_counts(sort=True).index[0]
print(f'The are with the largest frequency of night crimes: {peak_night_crime_location}')

# Identify the number of crimes committed against victims of different age groups.
# Save as a pandas Series called victim_ages, 
# with age group labels "0-17", "18-25", "26-34", "35-44", "45-54", "55-64", and "65+" 
# as the index and the frequency of crimes as the values.
victim_ages = ["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"]
age_conditions = [
    ((crimes['Vict Age'] > 0) & (crimes['Vict Age'] < 18)),
    ((crimes['Vict Age'] > 17) & (crimes['Vict Age'] < 26)),
    ((crimes['Vict Age'] > 25) & (crimes['Vict Age'] < 35)),
    ((crimes['Vict Age'] > 34) & (crimes['Vict Age'] < 45)),
    ((crimes['Vict Age'] > 44) & (crimes['Vict Age'] < 55)),
    ((crimes['Vict Age'] > 54) & (crimes['Vict Age'] < 65)),
    ((crimes['Vict Age'] > 64)),
]
# print((crimes['Vict Age'] > 0) & (crimes['Vict Age'] < 18))
crimes['age_category'] = np.select(age_conditions, victim_ages, default='xx')
# print(crimes.groupby(['age_category'])['age_category'].count())
print(f'The crimes committed against victimes of different age groups:')
print(crimes['age_category'].value_counts(sort=True))