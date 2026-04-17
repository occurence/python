"""
Replacing missing values
Another way of handling missing values is to replace them all with the same value. For numerical variables, one option is to replace values with 0— you'll do this here. However, when you replace missing values, you make assumptions about what a missing value means. In this case, you will assume that a missing number sold means that no sales for that avocado type were made that week.

In this exercise, you'll see how replacing missing values can affect the distribution of a variable using histograms. You can plot histograms for multiple variables at a time as follows:

dogs[["height_cm", "weight_kg"]].hist()
pandas has been imported as pd and matplotlib.pyplot has been imported as plt. The avocados_2016 dataset is available.
"""

# A list has been created, cols_with_missing, containing the names of columns with missing values: "small_sold", "large_sold", and "xl_sold".
# Create a histogram of those columns.
# Show the plot.

import pandas as pd
import matplotlib.pyplot as plt
avocados = pd.read_pickle(r"D:\STUDY\python\prep\04 data manipulation with pandas\datasets\avoplotto.pkl")
# avocados_2016 = avocados[pd.to_datetime(avocados['date']).dt.year == 2016]
avocados_2016 = pd.read_csv(r"D:\STUDY\python\prep\04 data manipulation with pandas\datasets\avocados_2016.csv", index_col=0)

# List the columns with missing values
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]

# Create histograms showing the distributions cols_with_missing
avocados_2016[cols_with_missing].hist()

# Show the plot
plt.show()

###########################################
###########################################
###########################################
# Replace the missing values of avocados_2016 with 0s and store the result as avocados_filled.
# Create a histogram of the cols_with_missing columns of avocados_filled

# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)

# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()

# Show the plot
plt.show()

# Fabulous filling! 
# Notice how the distribution has changed shape after replacing missing values with zeros.