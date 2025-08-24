import pandas as pd

gdp = pd.read_csv(r'D:\STUDY\python\Review\05 join pandas\datasets\gdp.csv')
pop = pd.read_csv(r'D:\STUDY\python\Review\05 join pandas\datasets\pop.csv')

# Merge gdp and pop on date and country with fill and notice rows 2 and 3
ctry_date = pd.merge_ordered(gdp, pop, on=['date', 'country'], 
                             fill_method='ffill')

# Print ctry_date
print(ctry_date)

# Merge gdp and pop on country and date with fill
date_ctry = pd.merge_ordered(gdp, pop, on=['country', 'date'],
                             fill_method='ffill')

# Print date_ctry
print(date_ctry)