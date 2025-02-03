import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
import numpy as np
from matplotlib.colors import ListedColormap
from sklearn.preprocessing import StandardScaler

wine = load_wine()
X, y = wine.data[:, :2], wine.target
y = (y < 2).astype(int) # Convert to binary classification
scaler = StandardScaler()
X = scaler.fit_transform(X)


def plot_4_classifiers(X, y, classifiers):
    """Plots decision boundaries for 4 classifiers."""
    h = 0.02  # Mesh step size
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))
    
    for idx, clf in enumerate(classifiers):
        ax = axes[idx]
        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        ax.contourf(xx, yy, Z, alpha=0.3)
        ax.scatter(X[:, 0], X[:, 1], c=y, edgecolor="k", cmap=ListedColormap(["r", "b"]))
        ax.set_title(clf.__class__.__name__)

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier

# Define the classifiers
classifiers = [LogisticRegression(solver='liblinear'), LinearSVC(), SVC(kernel="linear"), KNeighborsClassifier()]

# Fit the classifiers
for c in classifiers:
    c.fit(X, y)

# Plot the classifiers
plot_4_classifiers(X, y, classifiers)
plt.show()