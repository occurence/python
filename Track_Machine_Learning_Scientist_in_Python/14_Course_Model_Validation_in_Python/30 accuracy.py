import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import RandomizedSearchCV
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

rs = RandomizedSearchCV(cv=5, estimator=RandomForestClassifier(random_state=1111),
                   param_distributions={'max_depth': [2, 4, 8, 12],
                                        'min_samples_split': [2, 4, 6, 8],
                                        'n_estimators': [10, 20, 30]},
                   random_state=1111)
rs.fit(X, y)

print(rs.best_estimator_)
print("These parameters do produce the best testing accuracy. Good job! Remember, to reuse this model you can use rs.best_estimator_.")