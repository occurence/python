import pandas as pd
sales = pd.read_csv(r'D:\STUDY\python\Course_Data_Manipulation_Pandas\sales_subset.csv')

# Import numpy with the alias np
import numpy as np

# For each store type, aggregate weekly_sales: get min, max, mean, and median
# sales_stats = sales.groupby('type')['weekly_sales'].agg([np.min,np.max,np.mean,np.median])
sales_stats = sales.groupby('type')['weekly_sales'].agg(['min', 'max', 'mean', 'median'])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
# unemp_fuel_stats = sales.groupby('type')['unemployment','fuel_price_usd_per_l'].agg([np.min,np.max,np.mean,np.median])
unemp_fuel_stats = sales.groupby('type')[['unemployment', 'fuel_price_usd_per_l']].agg(['min', 'max', 'mean', 'median'])

# Print unemp_fuel_stats
print(unemp_fuel_stats)