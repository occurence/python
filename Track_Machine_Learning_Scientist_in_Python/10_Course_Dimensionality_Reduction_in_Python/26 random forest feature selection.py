import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

diabetes_df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\10_Course_Dimensionality_Reduction_in_Python\datasets\PimaIndians.csv')
X = diabetes_df.iloc[:, :-1]
y = diabetes_df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
rf = RandomForestClassifier(random_state=0)
rf.fit(X_train, y_train)
acc = accuracy_score(y_test, rf.predict(X_test))
print(dict(zip(X.columns, rf.feature_importances_.round(2))))


# Create a mask for features importances above the threshold
mask = rf.feature_importances_ > 0.15
print(mask)
# Apply the mask to the feature dataset X
reduced_X = X.loc[:, mask]

# prints out the selected column names
print(reduced_X.columns)