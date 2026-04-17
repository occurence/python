import pandas as pd
from sklearn_pandas import DataFrameMapper
from sklearn.impute import SimpleImputer

X = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\08_Course_Extreme_Gradient_Boosting_with_XGBoost\datasets\kidney_X.csv')
y = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\08_Course_Extreme_Gradient_Boosting_with_XGBoost\datasets\kidney_y.csv', header=None)
y = y[0].to_numpy()

kidney_feature_names = ['age','bp','sg','al','su','bgr','bu','sc','sod','pot','hemo','pcv','wc','rc','rbc','pc','pcc','ba','htn','dm','cad','appet','pe','ane']
nulls_per_column = X.isnull().sum()
# print(nulls_per_column)
categorical_feature_mask = X.dtypes == object
categorical_columns = X.columns[categorical_feature_mask].tolist()
non_categorical_columns = X.columns[~categorical_feature_mask].tolist()
numeric_imputation_mapper = DataFrameMapper( [([numeric_feature], SimpleImputer(strategy="median")) for numeric_feature in non_categorical_columns], input_df=True, df_out=True )
categorical_imputation_mapper = DataFrameMapper( [(category_feature, SimpleImputer()) for category_feature in categorical_columns], input_df=True, df_out=True )

# Import FeatureUnion
from sklearn.pipeline import FeatureUnion

# Combine the numeric and categorical transformations
numeric_categorical_union = FeatureUnion([
                                          ("num_mapper", numeric_imputation_mapper),
                                          ("cat_mapper", categorical_imputation_mapper)
                                         ])