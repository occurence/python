"""
Avocado supply and demand
Scatter plots are ideal for visualizing relationships between numerical variables. In this exercise, you'll compare the number of avocados sold to average price and see if they're at all related. If they're related, you may be able to use one number to predict the other.

matplotlib.pyplot has been imported as plt, pandas has been imported as pd, and avocados is available.
"""

# Create a scatter plot with nb_sold on the x-axis and avg_price on the y-axis. Title it "Number of avocados sold vs. average price".
# Show the plot.

import pandas as pd
import matplotlib.pyplot as plt
avocados = pd.read_pickle(r"D:\STUDY\python\prep\04 data manipulation with pandas\datasets\avoplotto.pkl")

# Scatter plot of avg_price vs. nb_sold with title
avocados.plot(x='nb_sold', y='avg_price', kind='scatter', title='Number of avocados sold vs. average price')

# Show the plot
plt.show()

# Super scatter plot! 
# It looks like when more avocados are sold, prices go down. 
# However, this doesn't mean that fewer sales causes higher prices - 
# we can only tell that they're correlated with each other.