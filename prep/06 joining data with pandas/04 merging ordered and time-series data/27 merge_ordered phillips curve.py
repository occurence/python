"""
Phillips curve using merge_ordered()
There is an economic theory developed by A. W. Phillips which states that inflation and unemployment have an inverse relationship. 
The theory claims that with economic growth comes inflation, which in turn should lead to more jobs and less unemployment.

You will take two tables of data from the U.S. Bureau of Labor Statistics, 
containing unemployment and inflation data over different periods, and create a Phillips curve. 
The tables have different frequencies. One table has a data entry every six months, while the other has a data entry every month. 
You will need to use the entries where you have data within both tables.

The tables unemployment and inflation have been loaded for you.
"""

# Use merge_ordered() to merge the inflation and unemployment tables on date with an inner join, and save the results as inflation_unemploy.
# Print the inflation_unemploy dataframe.
# Using inflation_unemploy, create a scatter plot with unemployment_rate on the horizontal axis and cpi (inflation) on the vertical axis.

import pandas as pd
import matplotlib.pyplot as plt

inflation = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\inflation.csv', index_col=0)
unemployment = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\unemployment.csv', index_col=0)

# Use merge_ordered() to merge inflation, unemployment with inner join
inflation_unemploy = pd.merge_ordered(inflation, unemployment, on='date', how='inner')

# Print inflation_unemploy 
print(inflation_unemploy)

# Plot a scatter plot of unemployment_rate vs cpi of inflation_unemploy
inflation_unemploy.plot(x='unemployment_rate', y='cpi', kind='scatter')
plt.show()

# Great work! You created a Phillips curve. 
# There are critics of the curve, but what is more important in this example is that you were able to use entries 
# where you had entries in both tables by using an inner join. 
# You might ask why not use the default outer join and use forward fill to fill to estimate the missing variables. 
# You might choose differently. 
# In this case, instead of showing an estimated unemployment rate (which is a continually changing measure) for five periods, 
# that data was dropped from the plot.