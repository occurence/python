import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split

cc = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\credit-card-full.csv')
# X_train = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\X_train.csv')
X = cc.iloc[:, :5]
# y = cc.iloc[:, -1]
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# sampled = cc.sample(1600, random_state=98170)
# # 9012, 14402, 40664, 85841, 98170
# print(sampled.index)


ohe = OneHotEncoder(sparse_output=False)
X_enc = ohe.fit_transform(X[['MARRIAGE']]).astype(int)
enc_columns = ohe.get_feature_names_out(['MARRIAGE'])
# X = pd.DataFrame(X_enc, columns=enc_columns)

X = pd.concat([X, pd.DataFrame(X_enc, columns=enc_columns)], axis=1)
print(X)