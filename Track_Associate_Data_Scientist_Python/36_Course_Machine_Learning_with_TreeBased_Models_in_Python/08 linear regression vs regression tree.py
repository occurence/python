import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as MSE

mpg = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\36_Course_Machine_Learning_with_TreeBased_Models_in_Python\datasets\auto.csv')
SEED = 1
mpg = pd.get_dummies(mpg, columns=['origin'], prefix='origin')
X = mpg.drop('mpg', axis=1).values
y = mpg['mpg'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEED) #stratify=y
from sklearn.tree import DecisionTreeRegressor
dt = DecisionTreeRegressor(max_depth=8, min_samples_leaf=0.13, random_state=3)
dt.fit(X_train, y_train)
y_pred = dt.predict(X_test)
mse_dt = MSE(y_test, y_pred)
rmse_dt = mse_dt**(1/2)

lr = LinearRegression()
lr.fit(X_train, y_train)

# Predict test set labels 
y_pred_lr = lr.predict(X_test)

# Compute mse_lr
mse_lr = MSE(y_test, y_pred_lr)

# Compute rmse_lr
rmse_lr = mse_lr**(1/2)

# Print rmse_lr
print('Linear Regression test set RMSE: {:.2f}'.format(rmse_lr))

# Print rmse_dt
print('Regression Tree test set RMSE: {:.2f}'.format(rmse_dt))