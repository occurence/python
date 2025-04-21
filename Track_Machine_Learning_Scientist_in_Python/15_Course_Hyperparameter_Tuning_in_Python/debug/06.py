import numpy as np

# Load the CSV back into a 2D array
flattened_data = np.loadtxt(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\tree.csv', delimiter=',', skiprows=1)

# Reshape the data back into the original 3D shape (359, 747, 4)
reshaped_data = flattened_data.reshape(359, 747, 4)

# Print the shape to confirm
print(reshaped_data.shape)  # Should print (359, 747, 4)
print(reshaped_data)