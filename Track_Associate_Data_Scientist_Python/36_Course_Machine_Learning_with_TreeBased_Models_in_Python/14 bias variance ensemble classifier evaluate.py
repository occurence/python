import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

liver = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\36_Course_Machine_Learning_with_TreeBased_Models_in_Python\datasets\indian_liver_patient_preprocessed.csv')
X = liver.drop('Is_male_std', axis=1).values
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# X = scaler.fit_transform(liver.drop('Is_male_std', axis=1).values)

y = liver['Is_male_std'].values
SEED=1
lr = LogisticRegression(random_state=SEED, solver="liblinear")
knn = KNeighborsClassifier(n_neighbors=27)
dt = DecisionTreeClassifier(min_samples_leaf=0.13, random_state=SEED)
classifiers = [('Logistic Regression', lr), ('K Nearest Neighbours', knn), ('Classification Tree', dt)]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=SEED)


# Iterate over the pre-defined list of classifiers
for clf_name, clf in classifiers:    
 
    # Fit clf to the training set
    clf.fit(X_train, y_train)    
   
    # Predict y_pred
    y_pred = clf.predict(X_test)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred) 
   
    # Evaluate clf's accuracy on the test set
    print('{:s} : {:.3f}'.format(clf_name, accuracy))

# print(liver.isna().sum().sort_values())