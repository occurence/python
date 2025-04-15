import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier

cc = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\creditcard.csv', index_col=0)
index = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\index.csv', index_col=0)
cc_base = cc.drop(['SEX', 'EDUCATION', 'MARRIAGE', 'default payment next month'], axis=1).astype(int)
cc_enc = cc[['SEX', 'EDUCATION', 'MARRIAGE']]
ohe = OneHotEncoder(sparse_output=False, drop= 'first')
enc = ohe.fit_transform(cc_enc).astype(int)
cc_enc_df = pd.DataFrame(enc, columns=ohe.get_feature_names_out())

X = pd.concat([cc_base, cc_enc_df], axis=1)

X_train = X.iloc[index.index]
# print(X_train)
y_train = cc[['default payment next month']].iloc[index.index]
y_train = y_train.values.ravel()
# print(y_train)

# rf_clf = RandomForestClassifier(max_depth=2)

# # Extract the 7th (index 6) tree from the random forest
# chosen_tree = rf_clf.estimators_[6]

# # Visualize the graph using the provided image
# imgplot = plt.imshow(tree_viz_image)
# plt.show()

# # Extract the parameters and level of the top (index 0) node
# split_column = chosen_tree.tree_.feature[0]
# split_column_name = X_train.columns[split_column]
# split_value = chosen_tree.tree_.threshold[0]

# # Print out the feature and level
# print("This node split on feature {}, at a value of {}".format(split_column_name, split_value))


tree_viz_image=pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\tree_viz_image.csv', header=None)
# print(tree)
# array_data = tree_viz_image.to_numpy()
# print(array_data.shape)
# # reshaped_data = array_data.reshape(359, 747, 4)
# reshaped_data = array_data.reshape(128880, 4)
# print(reshaped_data.shape)

# array_data = tree_viz_image.to_numpy()

# # Check the shape before reshaping
# print(array_data.shape)

# # Reshape back to original shape (359, 747, 4)
# reshaped_data = array_data.reshape(359, 747, 4)

# # Print the new shape
# print(reshaped_data.shape)

print(tree_viz_image.shape)