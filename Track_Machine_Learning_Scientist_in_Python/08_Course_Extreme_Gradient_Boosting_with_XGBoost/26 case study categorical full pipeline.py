import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn_pandas import DataFrameMapper
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.pipeline import FeatureUnion
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import cross_val_score
from sklearn.base import BaseEstimator, TransformerMixin

class Dictifier(BaseEstimator, TransformerMixin):       
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        if isinstance(X, np.ndarray):
            X = pd.DataFrame(X)
        return X.to_dict('records')

kidney_data = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\08_Course_Extreme_Gradient_Boosting_with_XGBoost\datasets\kidney.csv'
                          ,na_values='NaN')
with pd.option_context("future.no_silent_downcasting", True):
    y = kidney_data['class'].replace({'ckd': 0, 'notckd': 1}).infer_objects(copy=False)
X = kidney_data.iloc[:,:-1]

kidney_feature_names = ['age','bp','sg','al','su','bgr','bu','sc','sod','pot','hemo','pcv','wc','rc','rbc','pc','pcc','ba','htn','dm','cad','appet','pe','ane']
X = X[kidney_feature_names]
X = kidney_data.iloc[:,0:-1]
print(X)
nulls_per_column = X.isnull().sum()
# print(nulls_per_column)
categorical_feature_mask = X.dtypes == object
categorical_columns = X.columns[categorical_feature_mask].tolist()
non_categorical_columns = X.columns[~categorical_feature_mask].tolist()
# print(categorical_columns)
# print(non_categorical_columns)
# print(categorical_feature_mask)

numeric_imputation_mapper = DataFrameMapper( [([numeric_feature], SimpleImputer(strategy="median")) for numeric_feature in non_categorical_columns], input_df=True, df_out=True )
# categorical_imputation_mapper = DataFrameMapper( [(category_feature, SimpleImputer(strategy="most_frequent")) for category_feature in categorical_columns], input_df=True, df_out=True )
categorical_imputation_mapper = DataFrameMapper( [([category_feature], SimpleImputer(strategy="most_frequent")) for category_feature in categorical_columns], input_df=True, df_out=True )
numeric_categorical_union = FeatureUnion([
                                          ("num_mapper", numeric_imputation_mapper),
                                          ("cat_mapper", categorical_imputation_mapper)
                                         ])
# print(numeric_categorical_union)
# Create full pipeline
pipeline = Pipeline([
                     ("featureunion", numeric_categorical_union),
                     ("dictifier", Dictifier()),
                     ("vectorizer", DictVectorizer(sort=False)),
                     ("clf", xgb.XGBClassifier(max_depth=3))
                    ])

# Perform cross-validation
# cross_val_scores = cross_val_score(pipeline, kidney_data, y, scoring="roc_auc", cv=3)
cross_val_scores = cross_val_score(pipeline, X, y, scoring="roc_auc", cv=3)

# Print avg. AUC
print("3-fold AUC: ", np.mean(cross_val_scores))