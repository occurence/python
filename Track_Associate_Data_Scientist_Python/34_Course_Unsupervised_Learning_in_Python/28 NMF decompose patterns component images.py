import pandas as pd

df = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\34_Course_Unsupervised_Learning_in_Python\datasets\samples_LED.csv')
samples = df.to_numpy()

# Import pyplot
from matplotlib import pyplot as plt

# Select the 0th row: digit
digit = samples[0]

# Print digit
print(digit)

# Reshape digit to a 13x8 array: bitmap
bitmap = digit.reshape((13, 8))

# Print bitmap
print(bitmap)

# Use plt.imshow to display bitmap
plt.imshow(bitmap, cmap='gray', interpolation='nearest')
plt.colorbar()
plt.show()