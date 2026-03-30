"""
merge_ordered() caution, multiple columns
When using merge_ordered() to merge on multiple columns, the order is important when you combine it with the forward fill feature. 
The function sorts the merge on columns in the order provided. 
In this exercise, we will merge GDP and population data from the World Bank for Australia and Sweden, reversing the order of the merge on columns. 
The frequency of the series are different, the GDP values are quarterly, and the population is yearly. 
Use the forward fill feature to fill in the missing data. 
Depending on the order provided, the fill forward will use unintended data to fill in the missing values.

The tables gdp and pop have been loaded.
"""

# Use merge_ordered() on gdp and pop, merging on columns date and country with the fill feature, save to ctry_date.
# Perform the same merge of gdp and pop, but join on country and date (reverse of step 1) with the fill feature, saving this as date_ctry.

import pandas as pd

gdp = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\gdp_code.csv')
pop = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\pop.csv')

# Merge gdp and pop on date and country with fill and notice rows 2 and 3
# ctry_date = pd.merge_ordered(gdp, pop, on=['date', 'country'], 
#                              fill_method='ffill')
ctry_date = pd.merge_ordered(gdp, pop, on=['date', 'country'])
ctry_date[['date', 'country']] = ctry_date[['date', 'country']].ffill()

# Print ctry_date
print(ctry_date)

# Merge gdp and pop on country and date with fill
# date_ctry = pd.merge_ordered(gdp, pop, on=['country', 'date'], fill_method='ffill')
date_ctry = pd.merge_ordered(gdp, pop, on=['country', 'date'])
date_ctry[['country', 'date']] = date_ctry[['country', 'date']].ffill()

# Print date_ctry
print(date_ctry)

# Nice! When you merge on date first, the table is sorted by date then country. 
# When forward fill is applied, Sweden's population value in January is used to fill in the missing values for both Australia and Sweden for the remainder of the year. 
# This is not what you want. The fill forward is using unintended data to fill in the missing values. 
# However, when you merge on country first, the table is sorted by country then date, so the forward fill is applied appropriately in this situation.