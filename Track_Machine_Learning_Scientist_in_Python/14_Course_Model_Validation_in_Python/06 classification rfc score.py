import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

tictactoe = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\14_Course_Model_Validation_in_Python\datasets\tic-tac-toe.csv')

X = tictactoe.iloc[:, :-1]
y = tictactoe.iloc[:, -1]

ohe = OneHotEncoder(sparse_output=False)
X = ohe.fit_transform(X).astype(int)

le = LabelEncoder()
y = le.fit_transform(y).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=1111)

from sklearn.ensemble import RandomForestClassifier

# Create a random forest classifier
rfc = RandomForestClassifier(n_estimators=50, max_depth=6, random_state=1111)

# Fit rfc using X_train and y_train
rfc.fit(X_train, y_train)

# Create predictions on X_test
predictions = rfc.predict(X_test)
print(predictions[0:5])

# Print model accuracy using score() and the testing data
print(rfc.score(X_test, y_test))