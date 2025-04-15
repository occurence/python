import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

liver = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\36_Course_Machine_Learning_with_TreeBased_Models_in_Python\datasets\indian_liver_patient_preprocessed.csv')
SEED = 1
X = liver.drop('Is_male_std', axis=1).values
y = liver['Is_male_std'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=SEED)
dt = DecisionTreeClassifier(random_state=1)

params_dt = {'max_depth': [2,3,4],
             'min_samples_leaf': [0.12,0.14,0.16,0.18]}

grid_dt = GridSearchCV(estimator=dt,
                       param_grid=params_dt,
                       scoring='roc_auc',
                       cv=5,
                       n_jobs=-1)

grid_dt.fit(X_train, y_train)

# Import roc_auc_score from sklearn.metrics
from sklearn.metrics import roc_auc_score

# Extract the best estimator
best_model = grid_dt.best_estimator_

# Predict the test set probabilities of the positive class
y_pred_proba = grid_dt.predict_proba(X_test)[:,1]

# Compute test_roc_auc
test_roc_auc = roc_auc_score(y_test, y_pred_proba)

# Print test_roc_auc
print('Test set ROC AUC score: {:.3f}'.format(test_roc_auc))