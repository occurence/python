"""
Using merge_asof() to create dataset
The merge_asof() function can be used to create datasets where you have a table of start and stop dates, and you want to use them to create a flag in another table. 
You have been given gdp, which is a table of quarterly GDP values of the US during the 1980s. 
Additionally, the table recession has been given to you. 
It holds the starting date of every US recession since 1980, and the date when the recession was declared to be over. 
Use merge_asof() to merge the tables and create a status flag if a quarter was during a recession. 
Finally, to check your work, plot the data in a bar chart.

The tables gdp and recession have been loaded for you.
"""

# Using merge_asof(), merge gdp and recession on date, with gdp as the left table. Save to the variable gdp_recession.
# Create a list using a list comprehension and a conditional expression, named is_recession, where for each row if the gdp_recession['econ_status'] value is equal to 'recession' then enter 'r' else 'g'.
# Using gdp_recession, plot a bar chart of gdp versus date, setting the color argument equal to is_recession.

import pandas as pd
import matplotlib.pyplot as plt

gdp = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\gdp_recession.csv', index_col=0, parse_dates=[1])
recession = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\recession.csv', index_col=0, parse_dates=[1])

# Merge gdp and recession on date using merge_asof()
gdp_recession = pd.merge_asof(gdp, recession, on='date')
print(gdp_recession)
# Create a list based on the row value of gdp_recession['econ_status']
is_recession = ['r' if s=='recession' else 'g' for s in gdp_recession['econ_status']]

# Plot a bar chart of gdp_recession
gdp_recession.plot(kind='bar', y='gdp', x='date', color=is_recession, rot=90)
plt.show()

# Terrific work! 
# You can see from the chart that there were a number of quarters early in the 1980s where a recession was an issue. 
# merge_asof() allowed you to quickly add a flag to the gdp dataset by matching between two different dates, in one line of code! 
# If you were to perform the same task using subsetting, it would have taken a lot more code.