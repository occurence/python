import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error as mae

candies = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\14_Course_Model_Validation_in_Python\datasets\candy-data.csv')

X_train = np.array(candies.iloc[:50].drop(['competitorname', 'winpercent'], axis=1))
X_test = np.array(candies.iloc[50:].drop(['competitorname', 'winpercent'], axis=1))
y_train = np.array(candies.iloc[:50, -1])
y_test = np.array(candies.iloc[50:, -1])

model = RandomForestRegressor(n_estimators=50, random_state=1111)

# The model is fit using X_train and y_train
model.fit(X_train, y_train)

# Create vectors of predictions
train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)

# Train/Test Errors
train_error = mae(y_true=y_train, y_pred=train_predictions)
test_error = mae(y_true=y_test, y_pred=test_predictions)

# Print the accuracy for seen and unseen data
print("Model error on seen data: {0:.2f}.".format(train_error))
print("Model error on unseen data: {0:.2f}.".format(test_error))

print("When models perform differently on training and testing data, you should look to model validation to ensure you have the best performing model. In the next lesson, you will start building models to validate.")