"""
Price of conventional vs. organic avocados
Creating multiple plots for different subsets of data allows you to compare groups. In this exercise, you'll create multiple histograms to compare the prices of conventional and organic avocados.

matplotlib.pyplot has been imported as plt and pandas has been imported as pd.
"""

# Modify your code to use 20 bins in both histograms.
# Modify your code to adjust the transparency of both histograms to 0.5 to see how much overlap there is between the two distributions.
# Modify your code to use 20 bins in both histograms.

import pandas as pd
import matplotlib.pyplot as plt
avocados = pd.read_pickle(r"D:\STUDY\python\prep\04 data manipulation with pandas\datasets\avoplotto.pkl")

# Histogram of conventional avg_price 
avocados[avocados['type'] == 'conventional']['avg_price'].hist()

# Histogram of organic avg_price
avocados[avocados['type'] == 'organic']['avg_price'].hist()

# Add a legend
plt.legend(['conventional','organic'])

# Show the plot
plt.show()

###########################################
###########################################
###########################################

# Modify histogram transparency to 0.5 
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5)

# Modify histogram transparency to 0.5
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()

###########################################
###########################################
###########################################

# Modify bins to 20
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5, bins=20)

# Modify bins to 20
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins=20)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()

# Great layering! 
# 
# We can see that on average, organic avocados are more expensive than conventional ones, 
# but their price distributions have some overlap.