import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Import any additional modules and start coding below
rentals = pd.read_csv(r'D:\STUDY\python\rental_info.csv')

# print(rentals.loc[:,['rental_date']])
# print(rentals)
print(rentals['rental_date'])

