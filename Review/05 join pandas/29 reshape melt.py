import pandas as pd
import matplotlib.pyplot as plt

ur_wide = pd.read_csv(r'D:\STUDY\python\Review\05 join pandas\datasets\ur_wide.csv', index_col=0)

# unpivot everything besides the year column
ur_tall = ur_wide.melt(id_vars=['year'], var_name='month', value_name='unempl_rate')

# Create a date column using the month and year columns of ur_tall
# ur_tall['date'] = pd.to_datetime(ur_tall['year'] + '-' + ur_tall['month'])
ur_tall['date'] = pd.to_datetime(ur_tall['month'] + '-' + ur_tall['year'].astype(str))
print(ur_tall)

# Sort ur_tall by date in ascending order
ur_sorted = ur_tall.sort_values('date', ascending=True)

# Plot the unempl_rate by date
ur_sorted.plot('date', 'unempl_rate')
plt.show()