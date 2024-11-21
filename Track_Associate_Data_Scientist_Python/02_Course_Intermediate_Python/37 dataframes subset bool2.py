# Import cars data
import pandas as pd
cars = pd.read_csv('D:\STUDY\python\Course_Intermediate_Python\cars.csv', index_col = 0)

# Convert code to a one-liner
# sel = cars[['drives_right']]
print(cars[['drives_right']])
sel = cars[cars['drives_right']]

# Print sel
print(sel)