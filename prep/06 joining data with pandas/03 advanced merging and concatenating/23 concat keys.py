"""
Concatenating with keys
The leadership of the music streaming company has come to you and asked you for assistance in analyzing sales for a recent business quarter. 
They would like to know which month in the quarter saw the highest average invoice total. 
You have been given three tables with invoice data named inv_jul, inv_aug, and inv_sep. 
Concatenate these tables into one to create a graph of the average monthly invoice total.
"""

# Concatenate the three tables together vertically in order with the oldest month first, adding '7Jul', '8Aug', and '9Sep' as keys for their respective months, and save to inv_jul_thr_sep.
# Use the .agg() method to find the average of the total column from the grouped invoices.
# Create a bar chart of avg_inv_by_month.

import pandas as pd
import matplotlib.pyplot as plt

inv_jul = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\inv_jul.csv')
inv_aug = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\inv_aug.csv')
inv_sep = pd.read_csv(r'D:\STUDY\python\prep\06 joining data with pandas\datasets\inv_sep.csv')

# Concatenate the tables and add keys
inv_jul_thr_sep = pd.concat([inv_jul, inv_aug, inv_sep], 
                            keys=['7Jul', '8Aug', '9Sep'])

# Group the invoices by the index keys and find avg of the total column
avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total':'mean'})

# Bar plot of avg_inv_by_month
avg_inv_by_month.plot(kind='bar')
plt.show()