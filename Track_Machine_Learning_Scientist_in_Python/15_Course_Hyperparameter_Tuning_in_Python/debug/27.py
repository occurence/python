import pandas as pd
import numpy as np
from itertools import product
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import GradientBoostingClassifier

# Load data
cc = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\creditcard.csv', index_col=0)
index = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\train_index.csv', index_col=0)

# Preprocess
cc_base = cc.drop(['SEX', 'EDUCATION', 'MARRIAGE', 'default payment next month'], axis=1).astype(int)
cc_enc = cc[['SEX', 'EDUCATION', 'MARRIAGE']]
ohe = OneHotEncoder(sparse_output=False, drop='first')
enc = ohe.fit_transform(cc_enc).astype(int)
cc_enc_df = pd.DataFrame(enc, columns=ohe.get_feature_names_out())

X = pd.concat([cc_base, cc_enc_df], axis=1)
X_train = X.iloc[index.index]
y_train = cc[['default payment next month']].iloc[index.index].values.ravel()

# Hyperparameter ranges
x_lims = [0.01, 2.0]
y_lims = [3, 17]
z_lims = [1, 64]
learn_rate = np.linspace(x_lims[0], x_lims[1], 136)
min_samples_leaf = list(range(y_lims[0], y_lims[1]))
max_depth = list(range(z_lims[0], z_lims[1]))

# Sample 500 combinations
all_combinations = list(product(learn_rate, min_samples_leaf, max_depth))
np.random.seed(42)
sampled_indices = np.random.choice(len(all_combinations), size=500, replace=False)

# Function to compute accuracy table
def compute_accuracy_table(indices, run_name):
    rows = []
    for i, idx in enumerate(indices):
        lr, min_leaf, depth = all_combinations[idx]
        model = GradientBoostingClassifier(
            max_depth=depth,
            min_samples_leaf=min_leaf,
            learning_rate=lr
        )
        acc = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
        rows.append({
            'run': run_name,
            'index': i,
            'max_depth': depth,
            'min_samples_leaf': min_leaf,
            'learn_rate': lr,
            'accuracy': round(np.mean(acc) * 100)
        })
    return pd.DataFrame(rows)

# Run 1
df1 = compute_accuracy_table(sampled_indices, 'run_1')
print(df1)

# Run 2 (duplicate with same combinations)
df2 = compute_accuracy_table(sampled_indices, 'run_2')
print(df2)

# Optionally merge and compare
comparison = df1.merge(df2, on='index', suffixes=('_run1', '_run2'))
print(comparison[['index', 'accuracy_run1', 'accuracy_run2']])
