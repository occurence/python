import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Import any additional modules and start coding below
rentals = pd.read_csv('rental_info.csv')
# print(rentals)
# print(rentals[['rental_date']])
print(rentals.loc[:,['rental_date']])
# rental_length_days = pd.append
from datetime import datetime
# print(datetime.fromisoformat(rentals[['rental_date']]))
# print(datetime.fromisoformat(rentals.loc[:,['rental_date']]))
# print(pd.to_datetime(rentals.loc[:,['rental_date']]))
# print(pd.to_datetime(rentals['rental_date']))
# print(datetime.fromisoformat(pd.to_datetime(rentals['rental_date'])))
# print(rentals['rental_date'].iloc[0])
# print(datetime.fromisoformat(rentals['rental_date'].iloc[0]))
print(datetime.fromisoformat(rentals['return_date'].iloc[0]) - 
     datetime.fromisoformat(rentals['rental_date'].iloc[0]))