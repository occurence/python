import pandas as pd
import matplotlib.pyplot as plt

ten_yr = pd.read_csv(r'D:\STUDY\python\Review\05 join pandas\datasets\ten_yr.csv')
dji = pd.read_csv(r'D:\STUDY\python\Review\05 join pandas\datasets\dji.csv')

# Use melt on ten_yr, unpivot everything besides the metric column
bond_perc = ten_yr.melt(id_vars='metric', var_name='date', value_name='close')

# Use query on bond_perc to select only the rows where metric=close
bond_perc_close = bond_perc.query('metric == "close"')

# Merge (ordered) dji and bond_perc_close on date with an inner join
dow_bond = pd.merge_ordered(dji, bond_perc_close, on='date', how='inner', suffixes=('_dow', '_bond'))
print(dow_bond.head())

# Plot only the close_dow and close_bond columns
dow_bond.plot(y=['close_dow', 'close_bond'], x='date', rot=90)
plt.show()