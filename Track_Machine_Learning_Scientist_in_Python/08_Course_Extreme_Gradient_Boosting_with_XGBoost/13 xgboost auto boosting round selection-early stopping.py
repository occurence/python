import pandas as pd
import xgboost as xgb

housing = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\08_Course_Extreme_Gradient_Boosting_with_XGBoost\datasets\iowa.csv')
X, y = housing.iloc[:,:-1], housing.iloc[:,-1]

# Create your housing DMatrix: housing_dmatrix
housing_dmatrix = xgb.DMatrix(data=X, label=y)

# Create the parameter dictionary for each tree: params
params = {"objective":"reg:squarederror", "max_depth":4}

# Perform cross-validation with early stopping: cv_results
cv_results = xgb.cv(dtrain=housing_dmatrix, params=params, nfold=3, early_stopping_rounds=10, num_boost_round=50, metrics='rmse', as_pandas=True, seed=123)

# Print cv_results
print(cv_results)