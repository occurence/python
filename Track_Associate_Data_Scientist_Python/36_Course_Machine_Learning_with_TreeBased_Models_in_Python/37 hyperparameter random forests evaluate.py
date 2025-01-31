import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

bike = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\36_Course_Machine_Learning_with_TreeBased_Models_in_Python\datasets\bikes.csv')
SEED = 1
feature_names = bike.drop('cnt', axis=1).columns
X = bike.drop('cnt', axis=1).values
y = bike['cnt'].values
y_binned = pd.qcut(y, q=10, duplicates='drop', labels=False)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y_binned, random_state=SEED)
# params_rf = {'n_estimators': [100, 350, 500], 'max_features': ['log2', 'auto', 'sqrt'], 'min_samples_leaf': [2, 10, 30]}
params_rf = {'n_estimators': [100, 350, 500], 'max_features': ['sqrt'], 'min_samples_leaf': [2, 10, 30]}
rf = RandomForestRegressor(n_jobs=-1, random_state=2)

grid_rf = GridSearchCV(estimator=rf, param_grid=params_rf, scoring='neg_mean_squared_error', cv=3, verbose=1, n_jobs=-1)
grid_rf.fit(X_train, y_train)

# Import mean_squared_error from sklearn.metrics as MSE 
from sklearn.metrics import mean_squared_error as MSE

# Extract the best estimator
best_model = grid_rf.best_estimator_

# Predict test set labels
y_pred = best_model.predict(X_test)

# Compute rmse_test
rmse_test = MSE(y_test, y_pred)**(1/2)

# Print rmse_test
print('Test RMSE of best model: {:.3f}'.format(rmse_test)) 

# print(grid_rf.best_params_)