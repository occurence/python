# Import packages
import numpy as np
import matplotlib.pyplot as plt

# Assign filename to variable: file
file = r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\19_Course_Introduction_to_Importing_Data_in_Python\datasets\digits.csv'

# Load file as array: digits
digits = np.loadtxt(file, delimiter=',')

# Print datatype of digits
print(type(digits))

# Select and reshape a row
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))

# Plot reshaped data (matplotlib.pyplot already loaded as plt)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()
