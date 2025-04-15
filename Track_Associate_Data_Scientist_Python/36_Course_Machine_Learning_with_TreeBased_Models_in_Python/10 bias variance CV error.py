import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

mpg = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\36_Course_Machine_Learning_with_TreeBased_Models_in_Python\datasets\auto.csv')
SEED = 1
mpg = pd.get_dummies(mpg, columns=['origin'], prefix='origin')
mpg = mpg.astype({col: 'uint8' for col in mpg.select_dtypes(include='bool').columns})
X = mpg.drop('mpg', axis=1).values
y = mpg['mpg'].values
dt = DecisionTreeRegressor(max_depth=4, min_samples_leaf=0.26, random_state=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=SEED)

# Compute the array containing the 10-folds CV MSEs
MSE_CV_scores = - cross_val_score(dt, X_train, y_train, cv=10, 
                       scoring='neg_mean_squared_error',
                       n_jobs=-1)

# Compute the 10-folds CV RMSE
RMSE_CV = (MSE_CV_scores.mean())**(1/2)

# Print RMSE_CV
print('CV RMSE: {:.2f}'.format(RMSE_CV))