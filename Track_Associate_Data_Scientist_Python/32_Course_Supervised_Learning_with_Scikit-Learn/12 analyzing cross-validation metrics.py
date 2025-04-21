import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

sales_df = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\32_Course_Supervised_Learning_with_Scikit-Learn\datasets\sales_df.csv')
X = sales_df.drop("sales", axis=1).values
y = sales_df["sales"].values

from sklearn.model_selection import cross_val_score, KFold
kf = KFold(n_splits=6, shuffle=True, random_state=5)
reg = LinearRegression()
cv_results = cross_val_score(reg, X, y, cv=kf)
print(cv_results)
# cv_results = [0.74451678, 0.77241887, 0.76842114, 0.7410406, 0.75170022, 0.74406484]

# Print the mean
print(np.mean(cv_results))

# Print the standard deviation
print(np.std(cv_results))

# Print the 95% confidence interval
print(np.quantile(cv_results, [0.025, 0.975]))