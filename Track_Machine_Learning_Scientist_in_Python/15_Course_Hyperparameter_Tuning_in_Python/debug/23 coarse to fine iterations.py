import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import GradientBoostingClassifier

cc = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\creditcard.csv', index_col=0)
train_index = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\train_index.csv', index_col=0)
test_index = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\test_index.csv', index_col=0)

cc_base = cc.drop(['SEX', 'EDUCATION', 'MARRIAGE', 'default payment next month'], axis=1).astype(int)
cc_enc = cc[['SEX', 'EDUCATION', 'MARRIAGE']]
ohe = OneHotEncoder(sparse_output=False, drop= 'first')
enc = ohe.fit_transform(cc_enc).astype(int)
cc_enc_df = pd.DataFrame(enc, columns=ohe.get_feature_names_out())

cc_df = pd.concat([cc_base, cc_enc_df], axis=1)

X_train = cc_df.iloc[train_index.index]
y_train = cc[['default payment next month']].iloc[train_index.index].values.ravel()

X_test = cc_df.iloc[test_index.index]
y_test = cc[['default payment next month']].iloc[test_index.index].values.ravel()

# def visualize_first():
#   for name in results_df.columns[0:2]:
#     plt.clf()
#     plt.scatter(results_df[name],results_df['accuracy'], c=['blue']*500)
#     plt.gca().set(xlabel='{}'.format(name), ylabel='accuracy', title='Accuracy for different {}s'.format(name))
#     plt.gca().set_ylim([0,100])
#     x_line = 20
#     if name == "learn_rate":
#       	x_line = 1
#     plt.axvline(x=x_line, color="red", linewidth=4)
#     plt.show()

# def visualize_second():
#   for name in results_df2.columns[0:2]:
#     plt.clf()
#     plt.scatter(results_df2[name],results_df2['accuracy'], c=['blue']*1000)
#     plt.gca().set(xlabel='{}'.format(name), ylabel='accuracy', title='Accuracy for different {}s'.format(name))
#     plt.gca().set_ylim([0,100])
#     plt.show()


x_lims = [0.01, 1.0]
z_lims = [1, 20]

learn_rate = np.linspace(x_lims[0], x_lims[1], 50)
max_depth = list(range(z_lims[0],z_lims[1]))

combinations_list = [list(x) for x in product(max_depth, learn_rate)]

# print(combinations_list)

param_grid = {'max_depth': max_depth, 'learning_rate': learn_rate} 

random_GBM_class = RandomizedSearchCV(
    estimator = GradientBoostingClassifier(),
    param_distributions = param_grid,
    n_iter = 50, random_state=42,
    scoring='accuracy', n_jobs=4, cv = 5, refit=True, return_train_score = True)

random_GBM_class.fit(X_train, y_train)



results_list = []

tested_params = random_GBM_class.cv_results_['params']

for params in tested_params:
    model = GradientBoostingClassifier(**params)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    
    results_list.append([
        params.get('learning_rate'),
        # params.get('min_samples_leaf'),
        params.get('max_depth'),
        acc
    ])

results_df = pd.DataFrame(results_list, columns=[
    # 'learning_rate', 'min_samples_leaf', 'max_depth', 'accuracy'
    'learning_rate', 'max_depth', 'accuracy'
])

print(results_df.sort_values(by='accuracy', ascending=False))