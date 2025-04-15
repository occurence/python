import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error as MSE

bike = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\36_Course_Machine_Learning_with_TreeBased_Models_in_Python\datasets\bikes.csv')
SEED = 1
feature_names = bike.drop('cnt', axis=1).columns
X = bike.drop('cnt', axis=1).values
y = bike['cnt'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEED)#, stratify=y
rf = RandomForestRegressor(n_estimators=25,
            random_state=2)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
rmse_test = MSE(y_test, y_pred)**(1/2)
print('Test set RMSE of rf: {:.2f}'.format(rmse_test))

# Create a pd.Series of features importances
# importances = pd.Series(data=rf.feature_importances_, index=X_train.columns)
importances = pd.Series(data=rf.feature_importances_, index=feature_names)

# Sort importances
# importances_sorted = pd.Series(rf.feature_importances_, index=X_train.columns).sort_values()
importances_sorted = pd.Series(rf.feature_importances_, index=feature_names).sort_values()

# Draw a horizontal barplot of importances_sorted
importances_sorted.plot(kind='barh', color='lightgreen')
plt.title('Features Importances')
plt.show()