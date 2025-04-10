import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score
from sklearn.ensemble import GradientBoostingClassifier


cc = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\creditcard.csv', index_col=0)
train_index = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\400_train_index.csv', index_col=0)
test_index = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\100_test_index.csv', index_col=0)
cc_base = cc.drop(['SEX', 'EDUCATION', 'MARRIAGE', 'default payment next month'], axis=1).astype(int)
cc_enc = cc[['SEX', 'EDUCATION', 'MARRIAGE']]
ohe = OneHotEncoder(sparse_output=False, drop= 'first')
enc = ohe.fit_transform(cc_enc).astype(int)
cc_enc_df = pd.DataFrame(enc, columns=ohe.get_feature_names_out())

cc_df = pd.concat([cc_base, cc_enc_df], axis=1)

X_train = cc_df.iloc[train_index.index]
y_train = cc[['default payment next month']].iloc[train_index.index]
y_train = y_train.values.ravel()

X_test = cc_df.iloc[test_index.index]
y_test = cc[['default payment next month']].iloc[test_index.index]
y_test = y_test.values.ravel()

# Create the function
def gbm_grid_search(learning_rate, max_depth):

	# Create the model
    model = GradientBoostingClassifier(learning_rate=learning_rate, max_depth=max_depth)
    
    # Use the model to make predictions
    predictions = model.fit(X_train, y_train).predict(X_test)
    
    # Return the hyperparameters and score
    return([learning_rate, max_depth, accuracy_score(y_test, predictions)])