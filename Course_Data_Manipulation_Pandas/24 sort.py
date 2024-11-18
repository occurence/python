import pandas as pd
temperatures = pd.read_csv(r'D:\STUDY\python\Course_Data_Manipulation_Pandas\temperatures.csv')
temperatures_ind = temperatures.set_index(['country','city'])

# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level='city'))

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level=['country','city'], ascending=[True, False]))