import pandas as pd
import xgboost as xgb

churn_data = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\churn.csv')
X = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\decision_tree_X.csv').to_numpy()
y = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\decision_tree_y.csv', header=None)
y = y[0].to_numpy()

X, y = churn_data.iloc[:,:-1], churn_data.iloc[:,-1]
churn_dmatrix = xgb.DMatrix(data=X, label=y)
params = {"objective":"reg:logistic", "max_depth":3}

# Perform cross_validation: cv_results
cv_results = xgb.cv(dtrain=churn_dmatrix, params=params, 
                  nfold=3, num_boost_round=5, 
                  metrics="auc", as_pandas=True, seed=123)

# Print cv_results
print(cv_results)

# Print the AUC
print((cv_results["test-auc-mean"]).iloc[-1])
print("Fantastic! An AUC of 0.84 is quite strong. As you have seen, XGBoost's learning API makes it very easy to compute any metric you may be interested in. In Chapter 3, you'll learn about techniques to fine-tune your XGBoost models to improve their performance even further. For now, it's time to learn a little about exactly when to use XGBoost.")