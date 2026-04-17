"""
Square Brackets (2)
Square brackets can do more than just selecting columns. You can also use them to get rows, or observations, from a DataFrame. The following call selects the first five rows from the cars DataFrame:

cars[0:5]
The result is another DataFrame containing only the rows you specified.

Pay attention: You can only select rows using square brackets if you specify a slice, like 0:4. Also, you're using the integer indexes of the rows here, not the row labels!
"""

# Select the first 3 observations from cars and print them out.
# Select the fourth, fifth and sixth observation, corresponding to row indexes 3, 4 and 5, and print them out.

# Import cars data
import pandas as pd
cars = pd.read_csv(r"D:\STUDY\python\prep\02 intermediate\datasets\cars.csv", index_col = 0)

# Print out first 3 observations
print(cars[:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])

# Good job. You can get interesting information, but using square brackets to do indexing is rather limited. Experiment with more advanced techniques in the following exercises.