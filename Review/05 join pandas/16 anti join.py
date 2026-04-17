import pandas as pd

top_cust = pd.read_csv(r'D:\STUDY\python\Review\05 join pandas\datasets\top_cust.csv', index_col=0)
employees = pd.read_csv(r'D:\STUDY\python\Review\05 join pandas\datasets\employees.csv', index_col=0)

# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid', 
                                 how='left', indicator=True)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

# Get employees not working with top customers
print(employees[employees['srid'].isin(srid_list)])