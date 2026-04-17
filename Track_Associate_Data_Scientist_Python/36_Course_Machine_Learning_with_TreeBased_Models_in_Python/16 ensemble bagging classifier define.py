import pandas as pd

liver = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\36_Course_Machine_Learning_with_TreeBased_Models_in_Python\datasets\indian_liver_patient.csv')

# Import DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier 

# Import BaggingClassifier
from sklearn.ensemble import BaggingClassifier

# Instantiate dt
dt = DecisionTreeClassifier(random_state=1)

# Instantiate bc
# bc = BaggingClassifier(base_estimator=dt, n_estimators=50, random_state=1)
bc = BaggingClassifier(estimator=dt, n_estimators=50, random_state=1)