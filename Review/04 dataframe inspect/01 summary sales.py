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