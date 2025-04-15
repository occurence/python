import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error as mae
from sklearn.ensemble import RandomForestRegressor

candies = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\14_Course_Model_Validation_in_Python\datasets\candy-data.csv')
X = np.array(candies.iloc[:, 1:-1])
y = candies.iloc[:, -1]

from sklearn.model_selection import KFold

# Use KFold
kf = KFold(n_splits=5, shuffle=True, random_state=1111)

# Create splits
# splits = kf.split(X)
splits = list(kf.split(X))

# Print the number of indices
for train_index, val_index in splits:
    print("Number of training indices: %s" % len(train_index))
    print("Number of validation indices: %s" % len(val_index))

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

rfc = RandomForestRegressor(n_estimators=25, random_state=1111)

# Access the training and validation indices of splits
for train_index, val_index in splits:
    # Setup the training and validation data
    X_train, y_train = X[train_index], y[train_index]
    X_val, y_val = X[val_index], y[val_index]
    # Fit the random forest model
    rfc.fit(X_train, y_train)
    # Make predictions, and print the accuracy
    predictions = rfc.predict(X_val)
    print("Split accuracy: " + str(mean_squared_error(y_val, predictions)))

print("KFold() is a great method for accessing individual indices when completing cross-validation. One drawback is needing a for loop to work through the indices though. In the next lesson, you will look at an automated method for cross-validation using sklearn.")