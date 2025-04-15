import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\12_Course_Machine_Learning_for_Time_Series_Data_in_Python\datasets\iris.csv')

from sklearn.svm import LinearSVC

# Construct data for the model
X = iris[['petal length (cm)','petal width (cm)']]
y = iris[['target']].values

# Fit the model
model = LinearSVC()
model.fit(X, y.ravel())

# iris.plot(x='petal length (cm)', y='petal width (cm)', kind='scatter')
sns.scatterplot(x='petal length (cm)', y='petal width (cm)', data=iris, hue='target')
plt.show()