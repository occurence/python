import pandas as pd
import matplotlib.pyplot as plt

housing = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\12_Course_Machine_Learning_for_Time_Series_Data_in_Python\datasets\housing.csv')

from sklearn import linear_model

# Prepare input and output DataFrames
X = housing[['MedHouseVal']]
y = housing[['AveRooms']]

# Fit the model
model = linear_model.LinearRegression()
model.fit(X,y)

plt.scatter(X, y)
plt.show()