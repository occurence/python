import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier

X_train = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\multi_X_train.csv')
y_train = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\multi_y_train.csv', header=None)
X_test = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\multi_X_test.csv')
y_test = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\multi_y_test.csv', header=None)

# Fit one-vs-rest logistic regression classifier
# lr_ovr = LogisticRegression(multi_class='ovr')
# lr_ovr = LogisticRegression(solver='lbfgs', multi_class='ovr', max_iter=500)
lr_ovr = OneVsRestClassifier(LogisticRegression(solver='lbfgs', max_iter=1000))
lr_ovr.fit(X_train, y_train.values.ravel())

print("OVR training accuracy:", lr_ovr.score(X_train, y_train))
print("OVR test accuracy    :", lr_ovr.score(X_test, y_test))

# Fit softmax classifier
# lr_mn = LogisticRegression(multi_class='multinomial')
# lr_mn = LogisticRegression(solver='lbfgs', multi_class='multinomial', max_iter=500)
lr_mn = LogisticRegression(solver='lbfgs', max_iter=1000)
lr_mn.fit(X_train, y_train.values.ravel())

print("Softmax training accuracy:", lr_mn.score(X_train, y_train))
print("Softmax test accuracy    :", lr_mn.score(X_test, y_test))


print(type(y_train))