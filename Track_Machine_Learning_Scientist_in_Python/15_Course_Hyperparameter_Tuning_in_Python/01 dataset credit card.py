import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split

cc = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\creditcard.csv', index_col=0)
index = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\train_index.csv', index_col=0)
cc_base = cc.drop(['SEX', 'EDUCATION', 'MARRIAGE', 'default payment next month'], axis=1).astype(int)
cc_enc = cc[['SEX', 'EDUCATION', 'MARRIAGE']]
ohe = OneHotEncoder(sparse_output=False, drop= 'first')
enc = ohe.fit_transform(cc_enc).astype(int)
cc_enc_df = pd.DataFrame(enc, columns=ohe.get_feature_names_out())
# print(cc_enc_df)

X = pd.concat([cc_base, cc_enc_df], axis=1)
# print(X)

# print(cc.sample(1600).index)

X_train = X.iloc[index.index]
print(X_train)
y_train = cc[['default payment next month']].iloc[index.index]
y_train = y_train.values.ravel()
print(y_train)