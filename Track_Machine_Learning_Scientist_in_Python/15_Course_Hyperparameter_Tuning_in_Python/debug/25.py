import pandas as pd
import numpy as np
from itertools import product
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import GradientBoostingClassifier

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

learn_rate = np.linspace(x_lims[0], x_lims[1], 136)
min_samples_leaf = list(range(y_lims[0], y_lims[1]))
max_depth = list(range(z_lims[0],z_lims[1]))
# print(min_samples_leaf)

sampled_combinations = list(product(learn_rate, min_samples_leaf, max_depth))
np.random.seed(42)
sampled_combinations = np.random.choice(len(sampled_combinations), size=20, replace=False) 

# Create the parameter grid
param_grid = {'learning_rate': np.linspace(x_lims[0], x_lims[1], 136), 'min_samples_leaf': list(range(y_lims[0], y_lims[1])), 'max_depth': list(range(z_lims[0],z_lims[1]))} 

# Create a random search object
# random_GBM_class = RandomizedSearchCV(
#     estimator = GradientBoostingClassifier(),
#     param_distributions = param_grid,
#     n_iter = 500,
#     scoring='accuracy', n_jobs=4, cv = 5, refit=True, return_train_score = True)

# Fit to the training data
# random_GBM_class.fit(X_train, y_train)


# rows = []
# for i, idx in enumerate(sampled_combinations):
#     lr, min_leaf, depth = list(product(learn_rate, min_samples_leaf, max_depth))[idx]
#     model = GradientBoostingClassifier(
#         max_depth=depth,
#         min_samples_leaf=min_leaf,
#         learning_rate=lr
#     )
#     acc = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
#     rows.append({
#         'index': i,
#         'max_depth': depth,
#         'min_samples_leaf': min_leaf,
#         'learn_rate': lr,
#         'accuracy': round(np.mean(acc) * 100)
#     })

rows = []
lr, min_leaf, depth = 0.01, 11, 3

model = GradientBoostingClassifier(
    max_depth=depth,
    min_samples_leaf=min_leaf,
    learning_rate=lr
)
# acc = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
from sklearn.model_selection import KFold

cv = KFold(n_splits=5, shuffle=True, random_state=42)
acc = cross_val_score(model, X_train, y_train, cv=cv, scoring='accuracy')

rows.append({
    'max_depth': depth,
    'min_samples_leaf': min_leaf,
    'learn_rate': lr,
    'accuracy': round(np.mean(acc) * 100)
})

df = pd.DataFrame(rows)
print(df)