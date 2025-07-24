import pandas as pd

sales = pd.read_csv(r'D:\STUDY\python\Review\04 dataframe inspect\sales_subset.csv',index_col=0)

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby(['type'])['weekly_sales'].agg(['min','max','mean','median'])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby(['type'])[['unemployment','fuel_price_usd_per_l']].agg(['min','max','mean','median'])

# Print unemp_fuel_stats
print(unemp_fuel_stats)