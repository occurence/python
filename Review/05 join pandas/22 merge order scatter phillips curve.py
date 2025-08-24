import pandas as pd
import matplotlib.pyplot as plt

unemployment = pd.read_csv(r'D:\STUDY\python\Review\05 join pandas\datasets\unemployment.csv')
inflation = pd.read_csv(r'D:\STUDY\python\Review\05 join pandas\datasets\inflation.csv')

# Use merge_ordered() to merge inflation, unemployment with inner join
inflation_unemploy = pd.merge_ordered(inflation, unemployment, on='date', how='inner')

# Print inflation_unemploy 
print(inflation_unemploy)

# Plot a scatter plot of unemployment_rate vs cpi of inflation_unemploy
inflation_unemploy.plot(x='unemployment_rate', y='cpi', kind='scatter')
plt.show()