import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier

wine = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\11_Course_Preprocessing_for_Machine_Learning_in_Python\datasets\wine_types.csv')

pca = PCA()
X = wine.drop('Type', axis=1)
y = wine["Type"]
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
pca_X_train = pca.fit_transform(X_train)
pca_X_test = pca.transform(X_test)
print(pca.explained_variance_ratio_)

knn = KNeighborsClassifier()

# Fit knn to the training data
knn.fit(pca_X_train, y_train)

# Score knn on the test data and print it out
knn.score(pca_X_test, y_test)
print(knn.score(pca_X_test, y_test))