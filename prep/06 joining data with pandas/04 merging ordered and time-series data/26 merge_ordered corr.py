"""
Correlation between GDP and S&P500
In this exercise, you want to analyze stock returns from the S&P 500. 
You believe there may be a relationship between the returns of the S&P 500 and the GDP of the US. 
Merge the different datasets together to compute the correlation.

Two tables have been provided for you, named sp500, and gdp. 
As always, pandas has been imported for you as pd.
"""

# Use merge_ordered() to merge gdp and sp500 using a left join where the year column from gdp is matched with the date column from sp500.
# Print gdp_sp500.
# Use the merge_ordered() function again, similar to before, to merge gdp and sp500, using the function's ability to fill in missing data for returns by forward-filling the missing values. Assign the resulting table to the variable gdp_sp500.
# Subset the gdp_sp500 table, select the gdp and returns columns, and save as gdp_returns.
# Print the correlation matrix of the gdp_returns table using the .corr() method.

import pandas as pd

gdp = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\gdp.csv', index_col=0)
sp500 = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\S&P500.csv', index_col=0)

# Use merge_ordered() to merge gdp and sp500 on year and date
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', 
                             how='left')

# Print gdp_sp500
print(gdp_sp500)

# Use merge_ordered() to merge gdp and sp500, and forward fill missing values
# gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', 
#                              how='left', fill_method='ffill')
gdp_sp500['returns'] = gdp_sp500['returns'].ffill()

# Print gdp_sp500
print (gdp_sp500)

# Use merge_ordered() to merge gdp and sp500, and forward fill missing values
# gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', 
#                              how='left',  fill_method='ffill')

# Subset the gdp and returns columns
gdp_returns = gdp_sp500[['gdp', 'returns']]

# Print gdp_returns correlation
print (gdp_returns.corr())

# Awesome work! 
# You can see the different aspects of merge_ordered() and how you might use it on data that can be ordered. 
# By using this function, you were able to fill in the missing data from 2019. 
# Finally, the correlation of 0.21 between the GDP and S&P500 is low to moderate at best. 
# You may want to find another predictor if you plan to play in the stock market.