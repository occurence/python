import pandas as pd
import matplotlib.pyplot as plt

prices = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\12_Course_Machine_Learning_for_Time_Series_Data_in_Python\datasets\prices_stock_tech.csv')

# Plot the raw values over time
prices.plot()
plt.show()

# Scatterplot with one company per axis
prices.plot.scatter(x='EBAY', y='YHOO')
plt.show()

# Scatterplot with color relating to time
prices.plot.scatter('EBAY', 'YHOO', c=prices.index, 
                    cmap=plt.cm.viridis, colorbar=False)
plt.show()