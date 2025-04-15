import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ansur_df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\10_Course_Dimensionality_Reduction_in_Python\datasets\ansur_filter.csv')
# non_numeric = ['Branch', 'Gender', 'Component']
# df_numeric = ansur_df.drop(non_numeric, axis=1)
numeric_df = ansur_df.select_dtypes(include=[np.number])
# print(numeric_df.info())
# Calculate the correlation matrix and take the absolute value
corr_df = numeric_df.corr().abs()

# Create a True/False mask and apply it
mask = np.triu(np.ones_like(corr_df, dtype=bool))
tri_df = corr_df.mask(mask)

# List column names of highly correlated features (r > 0.95)
to_drop = [c for c in tri_df.columns if any(tri_df[c] >  0.95)]

# Drop the features in the to_drop list
reduced_df = ansur_df.drop(to_drop, axis=1)

print(f"The reduced_df DataFrame has {reduced_df.shape[1]} columns.")