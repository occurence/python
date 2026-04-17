# Import numpy
import numpy as np

# Assign the filename: file
file = r'D:\STUDY\python\Review\13 import data\datasets\digits_header.txt'

# Load the data: data
data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0, 1])

# Print data
print(data)