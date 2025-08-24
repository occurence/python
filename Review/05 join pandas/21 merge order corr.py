import pandas as pd

sp500 = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\06_Course_Joining_Data_Pandas\datasets\S&P500.csv')
gdp = pd.read_csv(r'D:\STUDY\python\Review\05 join pandas\datasets\WorldBank_GDP.csv')
gdp = gdp[gdp['Country Code'] == 'USA'][['Country Code', 'Year', 'GDP']]

# print(sp500)
# print(gdp)

# Use merge_ordered() to merge gdp and sp500, and forward fill missing values
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='Year', right_on='Date', 
                             how='left',  fill_method='ffill')

# Subset the gdp and returns columns
gdp_returns = gdp_sp500[['GDP', 'Returns']]

# Print gdp_returns correlation
print (gdp_returns.corr())