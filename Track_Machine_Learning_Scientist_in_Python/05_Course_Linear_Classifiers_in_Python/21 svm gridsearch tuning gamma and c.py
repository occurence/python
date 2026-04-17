import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

X_train = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\gamma_X_train.csv').to_numpy()
y_train = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\gamma_y_train.csv', header=None)
y_train = y_train[0].to_numpy()
X_test = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\gamma_X_test.csv').to_numpy()
y_test = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\gamma_y_test.csv', header=None)
y_test = y_test[0].to_numpy()

# Instantiate an RBF SVM
svm = SVC()

# Instantiate the GridSearchCV object and run the search
parameters = {'C':[0.1, 1, 10], 'gamma':[0.00001, 0.0001, 0.001, 0.01, 0.1]}
searcher = GridSearchCV(svm, parameters)
searcher.fit(X_train, y_train)

# Report the best parameters and the corresponding score
print("Best CV params", searcher.best_params_)
print("Best CV accuracy", searcher.best_score_)

# Report the test accuracy using these best parameters
print("Test accuracy of best grid search hypers:", searcher.score(X_test, y_test))