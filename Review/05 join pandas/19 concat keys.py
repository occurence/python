import pandas as pd
import matplotlib.pyplot as plt

inv_jul = pd.read_csv(r'D:\STUDY\python\Review\05 join pandas\datasets\inv_jul.csv')
inv_aug = pd.read_csv(r'D:\STUDY\python\Review\05 join pandas\datasets\inv_aug.csv')
inv_sep = pd.read_csv(r'D:\STUDY\python\Review\05 join pandas\datasets\inv_sep.csv')

# Concatenate the tables and add keys
inv_jul_thr_sep = pd.concat([inv_jul, inv_aug, inv_sep], 
                            keys=['7Jul', '8Aug', '9Sep'])

# Group the invoices by the index keys and find avg of the total column
avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total':'mean'})

# Bar plot of avg_inv_by_month
avg_inv_by_month.plot(kind='bar')
plt.show()