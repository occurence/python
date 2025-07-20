import pandas as pd
from sklearn.model_selection import train_test_split

train = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\25_Course_Winning_a_Kaggle_Competition_in_Python\datasets\taxi_train_chapter_4.csv')
test = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\25_Course_Winning_a_Kaggle_Competition_in_Python\datasets\taxi_test_chapter_4.csv')

validation_train, validation_test = train_test_split(train, test_size=0.3, random_state=123)

print(validation_train)
print(validation_test)

import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt

# Calculate the mean fare_amount on the validation_train data
naive_prediction = np.mean(validation_train['fare_amount'])

# Assign naive prediction to all the holdout observations
validation_test['pred'] = naive_prediction

# Measure the local RMSE
rmse = sqrt(mean_squared_error(validation_test['fare_amount'], validation_test['pred']))
print('Validation RMSE for Baseline I model: {:.3f}'.format(rmse))