import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import GradientBoostingClassifier

cc = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\creditcard.csv', index_col=0)
index = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\train_index.csv', index_col=0)
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

# combinations_list = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\combinations_list.csv')
# data = combinations_list.values.tolist()
x_lims = [0.01, 2.0]
y_lims = [3, 17]
z_lims = [1, 64]

learn_rate = np.linspace(x_lims[0], x_lims[1], 150)
min_samples_leaf = list(range(y_lims[0], y_lims[1]))
max_depth = list(range(z_lims[0],z_lims[1]))

combinations_list = [[z, y, x] for z in max_depth for y in min_samples_leaf for x in learn_rate]

print(type(combinations_list))
print(combinations_list[:5])

# def visualize_hyperparameter(name):
#   plt.clf()
#   plt.scatter(results_df[name],results_df['accuracy'], c=['blue']*500)
#   plt.gca().set(xlabel='{}'.format(name), ylabel='accuracy', title='Accuracy for different {}s'.format(name))
#   plt.gca().set_ylim([0,100])
#   plt.show()

rows = []
lr, min_leaf, depth = 0.01, 11, 3

model = GradientBoostingClassifier(
    max_depth=depth,
    min_samples_leaf=min_leaf,
    learning_rate=lr
)
acc = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
rows.append({
    'max_depth': depth,
    'min_samples_leaf': min_leaf,
    'learn_rate': lr,
    'accuracy': round(np.mean(acc) * 100)
})

df = pd.DataFrame(rows)
print(df)
