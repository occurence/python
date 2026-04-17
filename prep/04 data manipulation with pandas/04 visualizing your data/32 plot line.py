"""
Changes in sales over time
Line plots are designed to visualize the relationship between two numeric variables, where each data values is connected to the next one. They are especially useful for visualizing the change in a number over time since each time point is naturally connected to the next time point. In this exercise, you'll visualize the change in avocado sales over three years.

pandas has been imported as pd, and avocados is available.
"""

# Get the total number of avocados sold on each date. The DataFrame has two rows for each date—one for organic, and one for conventional. Save this as nb_sold_by_date.
# Create a line plot of the number of avocados sold.
# Show the plot.

import pandas as pd
avocados = pd.read_pickle(r"D:\STUDY\python\prep\04 data manipulation with pandas\datasets\avoplotto.pkl")

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby('date')['nb_sold'].sum()

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(x='date', y='nb_sold', kind='line')

# Show the plot
plt.show()

# Lovely line plot! 
# Line plots are great for visualizing something over time. 
# Here, it looks like the number of avocados spikes around the same time each year.