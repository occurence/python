import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

sales_df = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\32_Course_Supervised_Learning_with_Scikit-Learn\datasets\advertising_and_sales_clean.csv')

y = sales_df["sales"].values
X = sales_df["radio"].values.reshape(-1, 1)
reg = LinearRegression()
reg.fit(X, y)
predictions = reg.predict(X)
# print(predictions[:5])

# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Create scatter plot
plt.scatter(X, y, color="blue")

# Create line plot
plt.plot(X, predictions, color="red")
plt.xlabel("Radio Expenditure ($)")
plt.ylabel("Sales ($)")

# Display the plot
plt.show()