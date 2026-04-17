"""
Removing missing values
Now that you know there are some missing values in your DataFrame, you have a few options to deal with them. One way is to remove them from the dataset completely. In this exercise, you'll remove missing values by removing all rows that contain missing values.

pandas has been imported as pd and avocados_2016 is available.
"""

# Remove the rows of avocados_2016 that contain missing values and store the remaining rows in avocados_complete.
# Verify that all missing values have been removed from avocados_complete. Calculate each column that has NAs and print.

import pandas as pd
import matplotlib.pyplot as plt
avocados = pd.read_pickle(r"D:\STUDY\python\prep\04 data manipulation with pandas\datasets\avoplotto.pkl")
# avocados_2016 = avocados[pd.to_datetime(avocados['date']).dt.year == 2016]
avocados_2016 = pd.read_csv(r"D:\STUDY\python\prep\04 data manipulation with pandas\datasets\avocados_2016.csv", index_col=0)

# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())

# Delightful dropping! 
# Removing observations with missing values is a quick and dirty way to deal with missing data, 
# but this can introduce bias to your data if the values are not missing at random.