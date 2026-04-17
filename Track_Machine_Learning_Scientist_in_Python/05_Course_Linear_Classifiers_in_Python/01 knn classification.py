from scipy.sparse import csr_matrix
import pandas as pd
import numpy as np

df_X_train = pd.read_csv(r"D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\movie_X_train.csv")
# X_train_reconstructed = csr_matrix((df_X_train['value'], (df_X_train['row'], df_X_train['col'])), shape=(2000, 2500))  # Replace with actual shape
X_train = csr_matrix((df_X_train['value'], (df_X_train['row'], df_X_train['col'])), shape=(2000, 2500))  # Replace with actual shape

df_X_test = pd.read_csv(r"D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\movie_X_test.csv")
# X_test_reconstructed = csr_matrix((df_X_test['value'], (df_X_test['row'], df_X_test['col'])), shape=(500, 2500))  # Replace with actual shape
X_test = csr_matrix((df_X_test['value'], (df_X_test['row'], df_X_test['col'])), shape=(2000, 2500))  # Replace with actual shape

y_train = np.array(pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\movie_y_train.csv', header=None))

y_test = np.array(pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\movie_y_test.csv', header=None))

# print(type(y_test))

from sklearn.neighbors import KNeighborsClassifier

# Create and fit the model
knn = KNeighborsClassifier(n_neighbors=1)
# knn.fit(X_train, y_train)
knn.fit(X_train, y_train.ravel())

# Predict on the test features, print the results
pred = knn.predict(X_test)[0]
print("Prediction for test example 0:", pred)

# # print(X_test_reconstructed)

# # print("X_train rows:", df_X_train.shape[0])
# # print("X_test rows:", df_X_test.shape[0])

# print(type(X_train))
# print(X_train)