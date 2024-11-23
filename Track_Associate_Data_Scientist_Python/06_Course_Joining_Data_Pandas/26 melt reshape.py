import pandas as pd
import matplotlib.pyplot as plt

ur_wide = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\06_Course_Joining_Data_Pandas\datasets\ur_wide.csv')

# unpivot everything besides the year column
ur_tall = ur_wide.melt(id_vars='year', value_vars=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'], var_name='month', value_name='unempl_rate')


# Create a date column using the month and year columns of ur_tall
# ur_tall['date'] = pd.to_datetime(ur_tall['month'] + '-' + ur_tall['year'])
ur_tall['date'] = pd.to_datetime(ur_tall['month'] + '-' + ur_tall['year'].astype(str))

# Sort ur_tall by date in ascending order
ur_sorted = ur_tall.sort_values('date', ascending=True)

# Plot the unempl_rate by date
ur_sorted.plot(x='date', y='unempl_rate')
plt.show()