import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

housing = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\12_Course_Machine_Learning_for_Time_Series_Data_in_Python\datasets\housing.csv')
new_inputs = np.array(pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\12_Course_Machine_Learning_for_Time_Series_Data_in_Python\datasets\new_inputs.csv'))
# print(type(new_inputs))

from sklearn import linear_model

X = housing[['MedHouseVal']]
y = housing[['AveRooms']]
model = linear_model.LinearRegression()
model.fit(X,y)

# plt.scatter(X, y)
# plt.show()

# Generate predictions with the model using those inputs
predictions = model.predict(new_inputs.reshape(-1, 1))

# Visualize the inputs and predicted values
plt.scatter(new_inputs, predictions, color='r', s=3)
plt.xlabel('inputs')
plt.ylabel('predictions')
plt.show()

print("Here the red line shows the relationship that your model found. As the number of rooms grows, the median house value rises linearly.")