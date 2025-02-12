import pandas as pd
import numpy as np

X = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\decision_tree_X.csv').to_numpy()
y = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\decision_tree_y.csv', header=None)
y = y[0].to_numpy()

# Import the necessary modules
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Create the training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

# Instantiate the classifier: dt_clf_4
dt_clf_4 = DecisionTreeClassifier(max_depth=4)

# Fit the classifier to the training set
dt_clf_4.fit(X_train, y_train)

# Predict the labels of the test set: y_pred_4
y_pred_4 = dt_clf_4.predict(X_test)

# Compute the accuracy of the predictions: accuracy
accuracy = float(np.sum(y_pred_4==y_test))/y_test.shape[0]
print("accuracy:", accuracy)