import pandas as pd

sales = pd.read_csv(r'D:\STUDY\python\Review\04 dataframe inspect\sales_subset.csv')

print(sales.head())
print(sales.info())

# Summary Statistics
print(sales['weekly_sales'].mean())
print(sales['weekly_sales'].median())
# Aggregate Functions
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr,'median']))

# Cumulative Statistics
sales_1_1 = sales[(sales['store'] == 1) & (sales['department'] == 1)]
sales_1_1 = sales_1_1.sort_values('date', ascending=True)
sales_1_1['cum_weekly_sales'] = sales_1_1['weekly_sales'].cumsum()
sales_1_1['cum_max_sales'] = sales_1_1['weekly_sales'].cummax()
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])

# Count, Remove Duplicates and Categorical
store_types = sales.drop_duplicates(subset=['store','type'])
print(store_types.head())
store_depts = sales.drop_duplicates(subset=['store','department'])
print(store_depts.head())
holiday_dates = sales[sales['is_holiday']].drop_duplicates(subset='date')
print(holiday_dates['date'])

store_types = sales.drop_duplicates(subset=['store','type'])
store_depts = sales.drop_duplicates(subset=['store','department'])
holiday_dates = sales[sales['is_holiday']].drop_duplicates(subset='date')

store_counts = store_types['type'].value_counts()
print(store_counts)
store_props = store_types['type'].value_counts(normalize=True)
print(store_props)
dept_counts_sorted = store_depts['department'].value_counts(sort=True)
print(dept_counts_sorted)
dept_props_sorted = store_depts['department'].value_counts(sort=True, normalize=True)
print(dept_props_sorted)

# Manual Grouped Summary Statistics
sales_all = sales["weekly_sales"].sum()
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()
sales_B = sales[sales['type'] == 'B']['weekly_sales'].sum()
sales_C = sales[sales['type'] == 'C']['weekly_sales'].sum()
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)

# Grouped Summary Statistics
sales_by_type = sales.groupby("type")["weekly_sales"].sum()
sales_propn_by_type = sales_by_type / sum(sales_by_type)
print(sales_propn_by_type)
sales_by_type = sales.groupby("type")["weekly_sales"].sum()
sales_by_type_is_holiday = sales.groupby(['type','is_holiday'])['weekly_sales'].sum()
print(sales_by_type_is_holiday)

# Grouped Summary Statistics Agg
sales_stats = sales.groupby(['type'])['weekly_sales'].agg(['min','max','mean','median'])
print(sales_stats)
unemp_fuel_stats = sales.groupby(['type'])[['unemployment','fuel_price_usd_per_l']].agg(['min','max','mean','median'])
print(unemp_fuel_stats)