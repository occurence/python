import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import cross_val_score, RandomizedSearchCV
from sklearn.ensemble import GradientBoostingClassifier
import matplotlib.pyplot as plt

# Load data
cc = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\creditcard.csv', index_col=0)
index = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\train_index.csv', index_col=0)

# Preprocessing
cc_base = cc.drop(['SEX', 'EDUCATION', 'MARRIAGE', 'default payment next month'], axis=1).astype(int)
cc_enc = cc[['SEX', 'EDUCATION', 'MARRIAGE']]
ohe = OneHotEncoder(sparse_output=False, drop='first')
enc = ohe.fit_transform(cc_enc).astype(int)
cc_enc_df = pd.DataFrame(enc, columns=ohe.get_feature_names_out())

X = pd.concat([cc_base, cc_enc_df], axis=1)
X_train = X.iloc[index.index]
y_train = cc[['default payment next month']].iloc[index.index].values.ravel()

# --- Part 1: Manual single parameter run ---
rows = []
lr, min_leaf, depth = 0.050067114, 14, 7

model = GradientBoostingClassifier(
    max_depth=depth,
    min_samples_leaf=min_leaf,
    learning_rate=lr
)

acc = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
rows.append({
    'max_depth': depth,
    'min_samples_leaf': min_leaf,
    'learn_rate': lr,
    'accuracy': round(np.mean(acc) * 100)
})

df = pd.DataFrame(rows)
print("Manual single run result:")
print(df)

# --- Part 2: RandomizedSearchCV for broader tuning ---

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
    n_iter=10,  # Change to a higher number for better results
    scoring='accuracy',
    n_jobs=4,
    cv=5,
    refit=True,
    return_train_score=True,
    random_state=42
)

random_GBM_class.fit(X_train, y_train)

print("\nBest Parameters from RandomizedSearchCV:")
print(random_GBM_class.best_params_)
print("Best Accuracy Score: {:.2f}%".format(random_GBM_class.best_score_ * 100))

# Optional: Results dataframe
results_df = pd.DataFrame(random_GBM_class.cv_results_)
print("\nTop 5 Randomized Search Results:")
print(results_df[['params', 'mean_test_score', 'mean_train_score']].head())
