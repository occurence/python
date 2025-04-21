import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

weird_df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\10_Course_Dimensionality_Reduction_in_Python\datasets\weird_df.csv')

# Print the first five lines of weird_df
print(weird_df.head())

# Put nuclear energy production on the x-axis and the number of pool drownings on the y-axis
sns.scatterplot(x='nuclear_energy', y='pool_drownings', data=weird_df)
plt.show()

# Print out the correlation matrix of weird_df
print(weird_df.corr())

print("Not much, correlation does not imply causation.")