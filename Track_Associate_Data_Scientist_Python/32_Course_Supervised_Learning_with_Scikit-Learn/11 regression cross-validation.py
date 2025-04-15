import pandas as pd
from sklearn.linear_model import LinearRegression

sales_df = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\32_Course_Supervised_Learning_with_Scikit-Learn\datasets\sales_df.csv')
X = sales_df.drop("sales", axis=1).values
y = sales_df["sales"].values

# Import the necessary modules
from sklearn.model_selection import cross_val_score, KFold

# Create a KFold object
kf = KFold(n_splits=6, shuffle=True, random_state=100)

reg = LinearRegression()

# Compute 6-fold cross-validation scores
cv_scores = cross_val_score(reg, X, y, cv=kf)

# Print scores
print(cv_scores)

# for train_idx, test_idx in kf.split(X):
#     print("Train:", train_idx[:5], "Test:", test_idx[:5])  # Print first 5 indices