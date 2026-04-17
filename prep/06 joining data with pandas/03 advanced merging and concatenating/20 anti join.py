"""
Performing an anti join
In our music streaming company dataset, each customer is assigned an employee representative to assist them. In this exercise, filter the employee table by a table of top customers, returning only those employees who are not assigned to a customer. The results should resemble the results of an anti join. The company's leadership will assign these employees additional training so that they can work with high valued customers.

The top_cust and employees tables have been provided for you.
"""

# Merge employees and top_cust with a left join, setting indicator argument to True. Save the result to empl_cust.
# Select the srid column of empl_cust and the rows where _merge is 'left_only'. Save the result to srid_list.
# Subset the employees table and select those rows where the srid is in the variable srid_list and print the results.

import pandas as pd
employees = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\employees.csv')
top_cust = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\top_customer.csv')

# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid', 
                                 how='left', indicator=True)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

# Get employees not working with top customers
print(employees[employees['srid'].isin(srid_list)])

# Success! 
# You performed an anti join by first merging the tables with a left join, 
# selecting the ID of those employees who did not support a top customer, and then subsetting the original employee's table. 
# From that, we can see that there are five employees not supporting top customers. 
# Anti joins are a powerful tool to filter a main table (i.e. employees) by another (i.e. customers).