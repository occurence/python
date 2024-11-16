import pandas as pd
sales = pd.read_csv(r'D:\STUDY\python\Course_Data_Manipulation_Pandas\sales_subset.csv')

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=['store','type'])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=['store','department'])
print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales['is_holiday'] == True].drop_duplicates(subset=['date'])

# Print date col of holiday_dates
print(holiday_dates)