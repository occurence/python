import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error as mae

candies = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\14_Course_Model_Validation_in_Python\datasets\candy-data.csv')

X_train = np.array(candies.iloc[:50].drop(['competitorname', 'winpercent'], axis=1))
X_test = np.array(candies.iloc[50:].drop(['competitorname', 'winpercent'], axis=1))
y_train = np.array(candies.iloc[:50, -1])
y_test = np.array(candies.iloc[50:, -1])

rfr = RandomForestRegressor()

# Set the number of trees
rfr.n_estimators = 100

# Add a maximum depth
rfr.max_depth = 6

# Set the random state
rfr.seed = 111

# Fit the model
rfr.fit(X_train, y_train)