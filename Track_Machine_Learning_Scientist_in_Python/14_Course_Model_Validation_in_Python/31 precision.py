import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, make_scorer

tictactoe = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\14_Course_Model_Validation_in_Python\datasets\tic-tac-toe.csv')
X = tictactoe.iloc[:, :-1]
y = tictactoe.iloc[:, -1]

ohe = OneHotEncoder(sparse_output=False)
X_enc = ohe.fit_transform(X).astype(int)
enc_columns = ohe.get_feature_names_out(X.columns)
X = pd.DataFrame(X_enc, columns=enc_columns)

le = LabelEncoder()
y = le.fit_transform(y).astype(int)

rfc = RandomForestClassifier(random_state=1111)

param_dist = {'n_estimators': [10, 25, 50],
              'max_depth': range(2, 12, 2),
              'min_samples_split': range(2, 12, 2)}
# Create a precision scorer
precision = make_scorer(precision_score)
# Finalize the random search
rs = RandomizedSearchCV(
  estimator=rfc, param_distributions=param_dist,
  scoring = precision,
  cv=5, n_iter=10, random_state=1111)
rs.fit(X, y)

# print the mean test scores:
print('The accuracy for each run was: {}.'.format(rs.cv_results_['mean_test_score']))
# print the best model score:
print('The best accuracy for a single model was: {}'.format(rs.best_score_))

print("our model's precision was 93%! The best model accurately predicts a winning game 93% of the time. If you look at the mean test scores, you can tell some of the other parameter sets did really poorly. Also, since you used cross-validation, you can be confident in your predictions.")