import pandas as pd
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier

liver = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\36_Course_Machine_Learning_with_TreeBased_Models_in_Python\datasets\indian_liver_patient_preprocessed.csv')
SEED = 1
X = liver.drop('Is_male_std', axis=1).values
y = liver['Is_male_std'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=SEED)#
dt = DecisionTreeClassifier(max_depth=2, random_state=1)
# ada = AdaBoostClassifier(estimator=dt, n_estimators=180, random_state=SEED)
ada = AdaBoostClassifier(estimator=dt, n_estimators=180, algorithm="SAMME", random_state=SEED)

# Fit ada to the training set
ada.fit(X_train, y_train)

# Compute the probabilities of obtaining the positive class
y_pred_proba = ada.predict_proba(X_test)[:,1]