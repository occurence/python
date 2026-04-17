import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import RandomizedSearchCV

cc = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\creditcard.csv', index_col=0)
index = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\train_index.csv', index_col=0)
cc_base = cc.drop(['SEX', 'EDUCATION', 'MARRIAGE', 'default payment next month'], axis=1).astype(int)
cc_enc = cc[['SEX', 'EDUCATION', 'MARRIAGE']]
ohe = OneHotEncoder(sparse_output=False, drop= 'first')
enc = ohe.fit_transform(cc_enc).astype(int)
cc_enc_df = pd.DataFrame(enc, columns=ohe.get_feature_names_out())

X = pd.concat([cc_base, cc_enc_df], axis=1)

X_train = X.iloc[index.index]
# print(X_train)
y_train = cc[['default payment next month']].iloc[index.index]
y_train = y_train.values.ravel()
# print(y_train)

x_lims = [0.01, 2.0]
y_lims = [3, 17]
z_lims = [1, 64]

param_grid = {
    'learning_rate': np.linspace(x_lims[0], x_lims[1], 150),
    'min_samples_leaf': list(range(y_lims[0], y_lims[1])),
    'max_depth': list(range(z_lims[0], z_lims[1]))
}

random_GBM_class = RandomizedSearchCV(
    estimator=GradientBoostingClassifier(),
    param_distributions=param_grid,
    n_iter=10,  # You can increase this for better search
    scoring='accuracy',
    n_jobs=4,
    cv=5,
    refit=True,
    return_train_score=True,
    random_state=42
)

random_GBM_class.fit(X_train, y_train)

print("Best Parameters:", random_GBM_class.best_params_)
print("Best Score:", round(random_GBM_class.best_score_ * 100, 2))

results_df = pd.DataFrame(random_GBM_class.cv_results_)
print(results_df[['params', 'mean_test_score', 'mean_train_score']].head())
