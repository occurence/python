import pandas as pd

ansur_df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\10_Course_Dimensionality_Reduction_in_Python\datasets\ansur_large.csv')

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

scaler = StandardScaler()
ansur_std = scaler.fit_transform(ansur_df)
pca = PCA()
pca.fit(ansur_std)

# Inspect the explained variance ratio per component
print(pca.explained_variance_ratio_)
print("How much of the variance is explained by the 4th principal component? About 3.77%")

# Print the cumulative sum of the explained variance ratio
print(pca.explained_variance_ratio_.cumsum())
print("What's the lowest number of principal components you should keep if you don't want to lose more than 10% of explained variance during dimensionality reduction? 4 principal components")