import pandas as pd
import xgboost as xgb

df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\08_Course_Extreme_Gradient_Boosting_with_XGBoost\datasets\ames_unprocessed_data.csv')
X, y = df.iloc[:,:-1], df.iloc[:,-1]

# Import necessary modules
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import Pipeline

# Fill LotFrontage missing values with 0
X.LotFrontage = X['LotFrontage'].fillna(0)

# Setup the pipeline steps: steps
steps = [("ohe_onestep", DictVectorizer(sparse=False)),
         ("xgb_model", xgb.XGBRegressor())]

# Create the pipeline: xgb_pipeline
xgb_pipeline = Pipeline(steps)

# Fit the pipeline
xgb_pipeline.fit(X.to_dict('records'), y)