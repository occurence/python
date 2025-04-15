import pandas as pd

wine = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\11_Course_Preprocessing_for_Machine_Learning_in_Python\datasets\wine_types.csv')
X = wine[['Proline','Total phenols','Hue','Nonflavanoid phenols']]
y = wine[['Type']]
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier 

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

knn = KNeighborsClassifier()

# Fit the knn model to the training data
knn.fit(X_train, y_train)

# Score the model on the test data
print(knn.score(X_test, y_test))