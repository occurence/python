"""
Driving right (2)
The code in the previous example worked fine, but you actually unnecessarily created a new variable dr. You can achieve the same result without this intermediate variable. Put the code that computes dr straight into the square brackets that select observations from cars.
"""

# Convert the code to a one-liner that calculates the variable sel as before.

# Import cars data
import pandas as pd
cars = pd.read_csv(r"D:\STUDY\python\prep\02 intermediate\datasets\cars.csv", index_col = 0)

# Convert code to a one-liner
sel = cars[cars['drives_right']]

# Print sel
print(sel)

# Nice one! cars contains 7 rows or observations, sel contains 4; so in the majority of the countries in your dataset, people drive on the right side of the road.