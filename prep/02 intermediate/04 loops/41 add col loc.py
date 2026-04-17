"""
Add column (1)
In the video, Hugo showed you how to add the length of the country names of the brics DataFrame in a new column:

for lab, row in brics.iterrows() :
    brics.loc[lab, "name_length"] = len(row["country"])
You can do similar things on the cars DataFrame.
"""

# Use a for loop to add a new column, named COUNTRY, that contains a uppercase version of the country names in the "country" column. You can use the string method upper() for this.
# To see if your code worked, print out cars. Don't indent this code, so that it's not part of the for loop.

# Import cars data
import pandas as pd
cars = pd.read_csv(r"D:\STUDY\python\prep\02 intermediate\datasets\cars.csv", index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, 'COUNTRY'] = row['country'].upper()
# cars['country'].str.upper()
# Print cars
print(cars)

# Great, but you might remember that there is also an easier way to do this.