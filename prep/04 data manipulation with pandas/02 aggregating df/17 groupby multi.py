"""
Multiple grouped summaries
Earlier in this chapter, you saw that the .agg() method is useful to compute multiple statistics on multiple variables. It also works with grouped data. You can use built-in functions like min, max, mean, and median.

sales is available and pandas is imported as pd.
"""

# Get the min, max, mean, and median of weekly_sales for each store type using .groupby() and .agg(). Store this as sales_stats.
# Get the min, max, mean, and median of unemployment and fuel_price_usd_per_l for each store type. Store this as unemp_fuel_stats.

import pandas as pd
sales = pd.read_csv(r"D:\STUDY\python\prep\04 data manipulation with pandas\datasets\sales_subset.csv", index_col=0)

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby(['type'])['weekly_sales'].agg([min,max,'mean','median'])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby(['type'])[['unemployment','fuel_price_usd_per_l']].agg([min,max,'mean','median'])

# Print unemp_fuel_stats
print(unemp_fuel_stats)

# Awesome aggregating! 
# Notice that the minimum weekly_sales is negative because some stores had more returns than sales.