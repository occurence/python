import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

diabetes_df = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\32_Course_Supervised_Learning_with_Scikit-Learn\datasets\diabetes.csv')

X = diabetes_df.drop("diabetes", axis=1).values
y = diabetes_df["diabetes"].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred_probs = logreg.predict_proba(X_test)[:, 1]
# print(y_pred_probs[:10])

# Calculate roc_auc_score
print(roc_auc_score(y_test, y_pred_probs))

# Calculate the confusion matrix
print(confusion_matrix(y_test, y_pred))

# Calculate the classification report
print(classification_report(y_test, y_pred))