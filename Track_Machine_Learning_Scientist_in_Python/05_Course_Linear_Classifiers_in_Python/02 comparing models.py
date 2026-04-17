from scipy.sparse import csr_matrix
import pandas as pd
import numpy as np

df_X_train = pd.read_csv(r"D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\movie_X_train.csv")
X_train = csr_matrix((df_X_train['value'], (df_X_train['row'], df_X_train['col'])), shape=(2000, 2500))  # Replace with actual shape
df_X_test = pd.read_csv(r"D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\movie_X_test.csv")
X_test = csr_matrix((df_X_test['value'], (df_X_test['row'], df_X_test['col'])), shape=(2000, 2500))  # Replace with actual shape
y_train = np.array(pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\movie_y_train.csv', header=None))
y_test = np.array(pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\movie_y_test.csv', header=None))



from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Instantiate the model with k=1
knn1 = KNeighborsClassifier(n_neighbors=1)

# Fit the model to the training data
knn1.fit(X_train, y_train.ravel())

# Make predictions on the test set
y_pred1 = knn1.predict(X_test)

# Compute accuracy
accuracy1 = accuracy_score(y_test, y_pred1)

print("Test accuracy for k=1:", accuracy1)

# Repeat for k=5
knn5 = KNeighborsClassifier(n_neighbors=5)
knn5.fit(X_train, y_train.ravel())
y_pred5 = knn5.predict(X_test)
accuracy5 = accuracy_score(y_test, y_pred5)

print("Test accuracy for k=5:", accuracy5)
