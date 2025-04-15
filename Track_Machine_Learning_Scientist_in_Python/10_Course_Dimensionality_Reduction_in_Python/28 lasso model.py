import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso

ansur = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\10_Course_Dimensionality_Reduction_in_Python\datasets\ansur_filter.csv')
ansur_df = ansur.drop(['Branch', 'Gender', 'Component', 'weight_kg','stature_m','BMI_class','Height_class'], axis=1)
X = ansur_df.iloc[:, :-1]
y = ansur_df.iloc[:, -1]
scaler = StandardScaler()

# Set the test size to 30% to get a 70-30% train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Fit the scaler on the training features and transform these in one go
X_train_std = scaler.fit_transform(X_train)

# Create the Lasso model
la = Lasso(alpha=0.05)

# Fit it to the standardized training data
la.fit(X_train_std, y_train)