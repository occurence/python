import pandas as pd

# Read the CSV file
tree_viz_image = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\tree_viz_image.csv', header=None)

# # Convert to a NumPy array
# array_data = tree_viz_image.to_numpy()

# # Check the shape before reshaping
# print(array_data.shape)

# # The correct reshaping for (359, 747, 4) (if data is correct)
# reshaped_data = array_data.reshape(359, 747, 4)

# # Print the new shape
# print(reshaped_data.shape)

print(tree_viz_image.shape)