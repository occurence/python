import pandas as pd
import matplotlib.pyplot as plt

head_df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\10_Course_Dimensionality_Reduction_in_Python\datasets\head_df.csv')

# Create the boxplot
head_df.boxplot()

plt.show()

# Normalize the data
normalized_df = head_df / head_df.mean()

# Print the variances of the normalized data
print(normalized_df.var())

print("A threshold of 1.0e-03 (0.001) will remove the two low variance features.")