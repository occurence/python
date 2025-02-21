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

# Define Dictifier class to turn df into dictionary as part of pipeline
class Dictifier(BaseEstimator, TransformerMixin):       
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.to_dict('records')


kidney_data = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\08_Course_Extreme_Gradient_Boosting_with_XGBoost\datasets\kidney.csv')
X, y = kidney_data.iloc[:,:-1], kidney_data.iloc[:,-1]

kidney_data['age'] = pd.to_numeric(kidney_data['age'], errors='coerce')
kidney_data['bp'] = pd.to_numeric(kidney_data['bp'], errors='coerce')
kidney_data['sg'] = pd.to_numeric(kidney_data['sg'], errors='coerce')
kidney_data['al'] = pd.to_numeric(kidney_data['al'], errors='coerce')
kidney_data['su'] = pd.to_numeric(kidney_data['su'], errors='coerce')
kidney_data['bgr'] = pd.to_numeric(kidney_data['bgr'], errors='coerce')
kidney_data['bu'] = pd.to_numeric(kidney_data['bu'], errors='coerce')
kidney_data['sc'] = pd.to_numeric(kidney_data['sc'], errors='coerce')
kidney_data['sod'] = pd.to_numeric(kidney_data['sod'], errors='coerce')
kidney_data['pot'] = pd.to_numeric(kidney_data['pot'], errors='coerce')
kidney_data['hemo'] = pd.to_numeric(kidney_data['hemo'], errors='coerce')
kidney_data['pcv'] = pd.to_numeric(kidney_data['pcv'], errors='coerce')
kidney_data['wc'] = pd.to_numeric(kidney_data['wc'], errors='coerce')
kidney_data['rc'] = pd.to_numeric(kidney_data['rc'], errors='coerce')





kidney_feature_names = ['age','bp','sg','al','su','bgr','bu','sc','sod','pot','hemo','pcv','wc','rc','rbc','pc','pcc','ba','htn','dm','cad','appet','pe','ane']
nulls_per_column = X.isnull().sum()
# print(nulls_per_column)
categorical_feature_mask = X.dtypes == object
categorical_columns = X.columns[categorical_feature_mask].tolist()
non_categorical_columns = X.columns[~categorical_feature_mask].tolist()
# print(categorical_columns)
# print(non_categorical_columns)

numeric_imputation_mapper = DataFrameMapper( [([numeric_feature], SimpleImputer(strategy="median")) for numeric_feature in non_categorical_columns], input_df=True, df_out=True )
categorical_imputation_mapper = DataFrameMapper( [(category_feature, SimpleImputer()) for category_feature in categorical_columns], input_df=True, df_out=True )

numeric_categorical_union = FeatureUnion([
                                          ("num_mapper", numeric_imputation_mapper),
                                          ("cat_mapper", categorical_imputation_mapper)
                                         ])

# Create full pipeline
pipeline = Pipeline([
                     ("featureunion", numeric_categorical_union),
                     ("dictifier", Dictifier()),
                     ("vectorizer", DictVectorizer(sort=False)),
                     ("clf", xgb.XGBClassifier(max_depth=3))
                    ])

# Perform cross-validation
cross_val_scores = cross_val_score(pipeline, kidney_data, y, scoring="roc_auc", cv=3)

# Print avg. AUC
print("3-fold AUC: ", np.mean(cross_val_scores))