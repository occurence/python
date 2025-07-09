import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Read the train data
train = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\25_Course_Winning_a_Kaggle_Competition_in_Python\datasets\demand_forecasting_train_1_month.csv')

# Create a Random Forest object
rf = RandomForestRegressor()

# Train a model
rf.fit(X=train[['store', 'item']], y=train['sales'])

# Read test and sample submission data
test = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\25_Course_Winning_a_Kaggle_Competition_in_Python\datasets\demand_forecasting_test.csv')
sample_submission = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\25_Course_Winning_a_Kaggle_Competition_in_Python\datasets\demand_submission.csv')

# Show the head() of the sample_submission
print(sample_submission.head())

# Get predictions for the test set
test['sales'] = rf.predict(test[['store', 'item']])

# Write test predictions using the sample_submission format
test[['id', 'sales']].to_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\25_Course_Winning_a_Kaggle_Competition_in_Python\results\kaggle_submission.csv', index=False)

import xgboost as xgb

# Create DMatrix on train data
dtrain = xgb.DMatrix(data=train[['store', 'item']],
                     label=train['sales'])

# Define xgboost parameters
params = {'objective': 'reg:linear',
          'max_depth': 2,
          'verbosity': 0}

# Train xgboost model
xg_depth_2 = xgb.train(params=params, dtrain=dtrain)

# Define xgboost parameters
params = {'objective': 'reg:linear',
          'max_depth': 8,
          'verbosity': 0}

# Train xgboost model
xg_depth_8 = xgb.train(params=params, dtrain=dtrain)

# Define xgboost parameters
params = {'objective': 'reg:linear',
          'max_depth': 15,
          'verbosity': 0}

# Train xgboost model
xg_depth_15 = xgb.train(params=params, dtrain=dtrain)

from sklearn.metrics import mean_squared_error

dtrain = xgb.DMatrix(data=train[['store', 'item']])
dtest = xgb.DMatrix(data=test[['store', 'item']])

# For each of 3 trained models
for model in [xg_depth_2, xg_depth_8, xg_depth_15]:
    # Make predictions
    train_pred = model.predict(dtrain)     
    test_pred = model.predict(dtest)          
    
    # Calculate metrics
    mse_train = mean_squared_error(train['sales'], train_pred)                  
    mse_test = mean_squared_error(test['sales'], test_pred)
    print('MSE Train: {:.3f}. MSE Test: {:.3f}'.format(mse_train, mse_test))