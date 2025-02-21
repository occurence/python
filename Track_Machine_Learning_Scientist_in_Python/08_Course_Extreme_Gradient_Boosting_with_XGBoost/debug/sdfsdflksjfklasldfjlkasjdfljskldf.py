import pandas as pd
from sklearn_pandas import DataFrameMapper
from sklearn.impute import SimpleImputer
from sklearn_pandas import CategoricalImputer
from sklearn.pipeline import FeatureUnion, Pipeline
from sklearn.feature_extraction import DictVectorizer
import xgboost as xgb
from sklearn.model_selection import cross_val_score
from sklearn.base import BaseEstimator, TransformerMixin





kidney_feature_names = ['age',
                    'bp',
                    'sg',
                    'al',
                    'su',
                    'rbc',
                    'pc',
                    'pcc',
                    'ba',
                    'bgr',
                    'bu',
                    'sc',
                    'sod',
                    'pot',
                    'hemo',
                    'pcv',
                    'wc',
                    'rc',
                    'htn',
                    'dm',
                    'cad',
                    'appet',
                    'pe',
                    'ane',
                    'class']

kidney_data = pd.read_csv("https://assets.datacamp.com/production/repositories/943/datasets/82c231cd41f92325cf33b78aaa360824e6b599b9/chronic_kidney_disease.csv",
                      names=kidney_feature_names,
                      index_col=False,
                      na_values=["?"])

kidney_data['pcv'] = pd.to_numeric(kidney_data['pcv'], errors='coerce')
kidney_data['wc'] = pd.to_numeric(kidney_data['wc'], errors='coerce')
kidney_data['rc'] = pd.to_numeric(kidney_data['rc'], errors='coerce')
print(kidney_data.dtypes)

#Split data between data and labels
X, y = kidney_data.iloc[:,:-1], kidney_data.iloc[:, -1]

# Check number of nulls in each feature column
nulls_per_column = X.isnull().sum()
print(nulls_per_column)

# Create a boolean mask for categorical columns
categorical_feature_mask = X.dtypes == object
print(categorical_feature_mask)

# Get list of categorical column names
categorical_columns = X.columns[categorical_feature_mask].tolist()
print(categorical_columns)

# Get list of non-categorical column names
non_categorical_columns = X.columns[~categorical_feature_mask].tolist()
print(non_categorical_columns)



# Apply numeric imputer
numeric_imputation_mapper = DataFrameMapper(
                                        [([numeric_feature], SimpleImputer(strategy="median")) for 
numeric_feature in non_categorical_columns],
                                        input_df=True,
                                        df_out=True
                                       )

# Apply categorical imputer
categorical_imputation_mapper = DataFrameMapper(
                                            [(category_feature, CategoricalImputer()) for 
category_feature in categorical_columns],
                                            input_df=True,
                                            df_out=True
                                           )

# Combine the numeric and categorical transformations
numeric_categorical_union = FeatureUnion([
                                      ("num_mapper", numeric_imputation_mapper),
                                      ("cat_mapper", categorical_imputation_mapper)
                                     ])


# Custom transformer to convert Pandas DataFrame into Dict (needed for DictVectorizer)
class Dictifier(BaseEstimator, TransformerMixin):       
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.to_dict('records')

# Create full pipeline
pipeline = Pipeline([
                 ("featureunion", numeric_categorical_union),
                 ('dictifier', Dictifier())
                 ("vectorizer", DictVectorizer(sort=False)),
                 ("clf", xgb.XGBClassifier(max_depth=3))
                ])



# Perform cross-validation
cross_val_scores = cross_val_score(pipeline, X, y, scoring="roc_auc", cv=3)