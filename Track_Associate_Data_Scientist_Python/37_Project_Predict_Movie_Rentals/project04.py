import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Import any additional modules and start coding below
df_info = pd.read_csv('rental_info.csv')

df_info['rental_length'] = pd.to_datetime(df_info['return_date']) - pd.to_datetime(df_info['rental_date'])
df_info['rental_length_days'] = df_info['rental_length'].dt.days
print(df_info['special_features'])

df_info['deleted_scenes'] = np.where(df_info['special_features'].str.contains('Deleted Scenes'),1,0)
df_info['behind_the_scenes'] = np.where(df_info['special_features'].str.contains('Behind the Scenes'),1,0)

drop_columns = ['rental_date','return_date','rental_length','rental_length_days','special_features']

x = df_info.drop(drop_columns, axis=1)
y = df_info['rental_length_days']

print(np.where(df_info["special_features"].str.contains("Deleted Scenes"), 1, 0))