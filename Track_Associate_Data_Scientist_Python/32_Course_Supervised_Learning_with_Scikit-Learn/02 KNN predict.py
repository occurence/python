import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

churn_df = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\32_Course_Supervised_Learning_with_Scikit-Learn\datasets\churn_df.csv')

y = churn_df["churn"].values
X = churn_df[["account_length", "customer_service_calls"]].values
knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(X, y)

X_new = np.array([[30.0, 17.5],
                  [107.0, 24.1],
                  [213.0, 10.9]])

# Predict the labels for the X_new
y_pred = knn.predict(X_new)

# Print the predictions
print("Predictions: {}".format(y_pred))