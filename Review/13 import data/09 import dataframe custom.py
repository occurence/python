import pandas as pd

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Assign filename: file
file = r'D:\STUDY\python\Review\13 import data\datasets\titanic_corrupt.txt'

# Import file: data
data = pd.read_csv(file, sep='\t', comment='#', na_values=['Nothing'])

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()