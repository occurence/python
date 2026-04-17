import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

diabetes_df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\10_Course_Dimensionality_Reduction_in_Python\datasets\PimaIndians.csv')
y = diabetes_df.iloc[:, -1]

scaler = StandardScaler()
lr = LogisticRegression()

# Remove the feature with the lowest model coefficient
# Removing diastolic
X = diabetes_df[['pregnant', 'glucose', 'triceps', 'insulin', 'bmi', 'family', 'age']]

# Performs a 25-75% train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Scales features and fits the logistic regression model
lr.fit(scaler.fit_transform(X_train), y_train)

# Calculates the accuracy on the test set and prints coefficients
acc = accuracy_score(y_test, lr.predict(scaler.transform(X_test)))
print(f"{acc:.1%} accuracy on test set.") 
# print(dict(zip(X.columns, abs(lr.coef_[0]).round(2))))
d = dict(zip(X.columns, abs(lr.coef_[0]).round(2)))
d = sorted(d.items(), key=lambda item: item[1])
for key, value in d:
    print(f'{key} : {value}')