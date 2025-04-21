import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor

bike = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\36_Course_Machine_Learning_with_TreeBased_Models_in_Python\datasets\bikes.csv')
SEED = 1
feature_names = bike.drop('cnt', axis=1).columns
X = bike.drop('cnt', axis=1).values
y = bike['cnt'].values
y_binned = pd.qcut(y, q=10, duplicates='drop', labels=False)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y_binned, random_state=SEED)

sgbr = GradientBoostingRegressor(max_depth=4, subsample=0.9, max_features=0.75, n_estimators=200, random_state=2)
sgbr.fit(X_train, y_train)
y_pred = sgbr.predict(X_test)

# Import mean_squared_error as MSE
from sklearn.metrics import mean_squared_error as MSE

# Compute test set MSE
mse_test = MSE(y_test, y_pred)

# Compute test set RMSE
rmse_test = mse_test**(1/2)

# Print rmse_test
print('Test set RMSE of sgbr: {:.3f}'.format(rmse_test))