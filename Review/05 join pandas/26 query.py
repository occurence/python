import pandas as pd

social_fin = pd.read_csv(r'D:\STUDY\python\Review\05 join pandas\datasets\social_fin.csv')
print(social_fin['financial'].value_counts())

# There 2 rows where the value is greater than $50,000,000K.
print(social_fin.query('value > 50000000'))

# There are 3 rows for total revenue for Facebook.
print(social_fin.query('company == "facebook" and financial =="total_revenue"'))

# There are 6 rows where the net income has a negative value.
print(social_fin.query('financial =="net_income" and value < 0'))

# There are 45 rows, where the gross profit is greater than $100K.
print(social_fin.query('financial == "gross_profit" and value > 100'))