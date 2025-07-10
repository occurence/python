import numpy as np
import pandas as pd

# Import MSE from sklearn
from sklearn.metrics import mean_squared_error

# Define your own MSE function
def own_mse(y_true, y_pred):
  	# Raise differences to the power of 2
    squares = np.power(y_true - y_pred, 2)
    # Find mean over all observations
    err = np.mean(squares)
    return err

y_regression_true = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\25_Course_Winning_a_Kaggle_Competition_in_Python\datasets\regression_true.csv', header=None).to_numpy()
y_regression_pred = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\25_Course_Winning_a_Kaggle_Competition_in_Python\datasets\regression_predict.csv', header=None).to_numpy()

print('Sklearn MSE: {:.5f}. '.format(mean_squared_error(y_regression_true, y_regression_pred)))
print('Your MSE: {:.5f}. '.format(own_mse(y_regression_true, y_regression_pred)))