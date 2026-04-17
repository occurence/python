import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import GridSearchCV

housing = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\08_Course_Extreme_Gradient_Boosting_with_XGBoost\datasets\iowa.csv')
X, y = housing.iloc[:,:-1], housing.iloc[:,-1]

# Create the parameter grid: gbm_param_grid
gbm_param_grid = {
    'colsample_bytree': [0.3, 0.7],
    'n_estimators': [50],
    'max_depth': [2, 5]
}

# Instantiate the regressor: gbm
gbm = xgb.XGBRegressor()

# Perform grid search: grid_mse
grid_mse = GridSearchCV(estimator=gbm,param_grid=gbm_param_grid, scoring='neg_mean_squared_error', cv=4, verbose=1)


# Fit grid_mse to the data
grid_mse.fit(X, y)

# Print the best parameters and lowest RMSE
print("Best parameters found: ", grid_mse.best_params_)
print("Lowest RMSE found: ", np.sqrt(np.abs(grid_mse.best_score_)))