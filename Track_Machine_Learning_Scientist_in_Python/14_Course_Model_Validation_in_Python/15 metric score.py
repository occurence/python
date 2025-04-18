import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.ensemble import RandomForestClassifier

tictactoe = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\14_Course_Model_Validation_in_Python\datasets\tic-tac-toe.csv')

X = tictactoe.iloc[:, :-1]
y = tictactoe.iloc[:, -1]

ohe = OneHotEncoder(sparse_output=False)
X_enc = ohe.fit_transform(X).astype(int)
enc_columns = ohe.get_feature_names_out(X.columns)
X = pd.DataFrame(X_enc, columns=enc_columns)

le = LabelEncoder()
y = le.fit_transform(y).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.9, random_state=1111)

rfc = RandomForestClassifier(n_estimators=500, random_state=1111)
rfc.fit(X_train, y_train)

from sklearn.metrics import confusion_matrix

# Create predictions
test_predictions = rfc.predict(X_test)

# Create and print the confusion matrix
cm = confusion_matrix(y_test, test_predictions)
print(cm)

# Print the true positives (actual 1s that were predicted 1s)
print("The number of true positives is: {}".format(cm[1, 1]))


from sklearn.metrics import accuracy_score, precision_score, recall_score

test_predictions = rfc.predict(X_test)

# Create precision or recall score based on the metric you imported
score = precision_score(y_test, test_predictions)

# Print the final result
print("The precision value is {0:.2f}".format(score))

print("Precision is the correct metric here. Sore-losers can't stand losing when they are certain they will win! For that reason, our model needs to be as precise as possible. With a precision of only 79%, you may need to try some other modeling techniques to improve this score.")