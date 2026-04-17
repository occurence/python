import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from mlxtend.plotting import plot_decision_regions

wbc = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\36_Course_Machine_Learning_with_TreeBased_Models_in_Python\datasets\wbc.csv')
SEED = 1
selected_features = ['radius_mean', 'concave points_mean']
X = wbc[selected_features].values
y = wbc['diagnosis'].values
y = np.where(y == 'M', 1, 0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=SEED)
dt = DecisionTreeClassifier(max_depth=6, random_state=SEED)
dt.fit(X_train, y_train)
y_pred = dt.predict(X_test)

def plot_labeled_decision_regions(X, y, models):
    fig, ax = plt.subplots(1, 2, figsize=(6.0, 2.7), sharey=True)
    for i, model in enumerate(models):
        plot_decision_regions(X, y, clf=model, ax=ax[i])
        ax[i].set_title(model.__class__.__name__)
        ax[i].set_xlabel('Radius Mean')
        if i == 0:
            ax[i].set_ylabel('Concave Points Mean')
    plt.tight_layout()
    plt.show()


# Import LogisticRegression from sklearn.linear_model
from sklearn.linear_model import  LogisticRegression

# Instatiate logreg
logreg = LogisticRegression(random_state=1)

# Fit logreg to the training set
logreg.fit(X_train, y_train)

# Define a list called clfs containing the two classifiers logreg and dt
clfs = [logreg, dt]

# Review the decision regions of the two classifiers
plot_labeled_decision_regions(X_test, y_test, clfs)

print(y_test)