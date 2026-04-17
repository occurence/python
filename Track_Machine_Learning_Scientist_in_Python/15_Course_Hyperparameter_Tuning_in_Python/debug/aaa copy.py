import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import product
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

# results_df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\results_df.csv')
x_lims = [0.01, 2.0]
y_lims = [3, 17]
z_lims = [1, 64]

learn_rate = np.linspace(x_lims[0], x_lims[1], 150)
min_samples_leaf = list(range(y_lims[0], y_lims[1]))
max_depth = list(range(z_lims[0],z_lims[1]))

# combinations_list = [[z, y, x] for z in max_depth for y in min_samples_leaf for x in learn_rate]
combinations_list = [list(x) for x in product(max_depth, min_samples_leaf, learn_rate)]
print(len(combinations_list))

# Create the parameter grid
param_grid = {'learning_rate': learn_rate, 'min_samples_leaf': min_samples_leaf, 'max_depth': max_depth} 

# Create a random search object
random_GBM_class = RandomizedSearchCV(
    estimator = GradientBoostingClassifier(),
    param_distributions = param_grid,
    n_iter = 10, random_state=42,
    scoring='accuracy', n_jobs=4, cv = 5, refit=True, return_train_score = True)

# Fit to the training data
random_GBM_class.fit(X_train, y_train)

from sklearn.metrics import accuracy_score

# Initialize results list
results_list = []

# Get all parameter combinations tested by RandomizedSearchCV
tested_params = random_GBM_class.cv_results_['params']

# Loop through each set of tested hyperparameters
for params in tested_params:
    model = GradientBoostingClassifier(**params)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    
    # You can also store other params if needed
    results_list.append([
        params.get('learning_rate'),
        params.get('min_samples_leaf'),
        params.get('max_depth'),
        acc
    ])

# Optionally convert to DataFrame for easy viewing or saving
results_df = pd.DataFrame(results_list, columns=[
    'learning_rate', 'min_samples_leaf', 'max_depth', 'accuracy'
])

print(results_df.sort_values(by='accuracy', ascending=False))


# print(random_GBM_class.cv_results_['param_learning_rate'])
# print(random_GBM_class.cv_results_['param_min_samples_leaf'])


# def visualize_hyperparameter(name):
#   plt.clf()
#   plt.scatter(results_df[name],results_df['accuracy'], c=['blue']*500)
#   plt.gca().set(xlabel='{}'.format(name), ylabel='accuracy', title='Accuracy for different {}s'.format(name))
#   plt.gca().set_ylim([0,100])
#   plt.show()

# # Confirm the size of the combinations_list
# print(len(combinations_list))

# # Sort the results_df by accuracy and print the top 10 rows
# print(results_df.sort_values(by='accuracy', ascending=False).head(10))

# # Confirm which hyperparameters were used in this search
# print(results_df.columns)

# # Call visualize_hyperparameter() with each hyperparameter in turn
# visualize_hyperparameter('max_depth')
# visualize_hyperparameter('min_samples_leaf')
# visualize_hyperparameter('learn_rate')