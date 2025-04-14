import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score

# Load data
cc = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\creditcard.csv', index_col=0)
index = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\train_index.csv', index_col=0)

# One-hot encode categorical features
cc_base = cc.drop(['SEX', 'EDUCATION', 'MARRIAGE', 'default payment next month'], axis=1).astype(int)
cc_enc = cc[['SEX', 'EDUCATION', 'MARRIAGE']]
ohe = OneHotEncoder(sparse_output=False, drop='first')
enc = ohe.fit_transform(cc_enc).astype(int)
cc_enc_df = pd.DataFrame(enc, columns=ohe.get_feature_names_out())

# Concatenate encoded and numeric features
X = pd.concat([cc_base, cc_enc_df], axis=1)

# Create train and test sets
X_train = X.iloc[index.index]
y_train = cc[['default payment next month']].iloc[index.index].values.ravel()
X_test = X.drop(index.index)
y_test = cc[['default payment next month']].drop(index.index).values.ravel()

# Load previous results for visualization
results_df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\results_df.csv')

# Define hyperparameter ranges
x_lims = [0.01, 2.0]
y_lims = [3, 17]
z_lims = [1, 64]

learn_rate = np.linspace(x_lims[0], x_lims[1], 150)
min_samples_leaf = list(range(y_lims[0], y_lims[1]))
max_depth = list(range(z_lims[0], z_lims[1]))

combinations_list = [list(x) for x in product(max_depth, min_samples_leaf, learn_rate)]
print("Total hyperparameter combinations:", len(combinations_list))

def visualize_hyperparameter(name):
    plt.clf()
    plt.scatter(results_df[name], results_df['accuracy'], c=['blue'] * 500)
    plt.gca().set(xlabel=name, ylabel='accuracy', title=f'Accuracy for different {name}s')
    plt.gca().set_ylim([0, 100])
    plt.show()

# Print sorted top results
print(results_df.sort_values(by='accuracy', ascending=False).head(10))
print("Hyperparameter columns used:", results_df.columns)

# Visualize each hyperparameter
visualize_hyperparameter('max_depth')
visualize_hyperparameter('min_samples_leaf')
visualize_hyperparameter('learn_rate')

# Set up hyperparameter grid
param_grid = {
    'learning_rate': learn_rate,
    'min_samples_leaf': min_samples_leaf,
    'max_depth': max_depth
}

# Set up RandomizedSearchCV
random_GBM_class = RandomizedSearchCV(
    estimator=GradientBoostingClassifier(),
    param_distributions=param_grid,
    n_iter=10,
    scoring='accuracy',
    n_jobs=4,
    cv=5,
    refit=True,
    return_train_score=True
)

# Fit model
random_GBM_class.fit(X_train, y_train)

# Print tested hyperparameter values
print("Tested learning rates:", random_GBM_class.cv_results_['param_learning_rate'])
print("Tested min_samples_leaf:", random_GBM_class.cv_results_['param_min_samples_leaf'])

# Predict on test set using best model
best_model = random_GBM_class.best_estimator_
predictions = best_model.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, predictions)

# Save results
results_list = []
learning_rate = random_GBM_class.best_params_['learning_rate']
results_list.append([learning_rate, accuracy])

print("Best learning rate:", learning_rate)
print("Test set accuracy:", accuracy)
