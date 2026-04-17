import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error as mae

candies = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\14_Course_Model_Validation_in_Python\datasets\candy-data.csv')

X = candies.iloc[:, 1:-1]
y = candies.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1111)

features_list = [2, 4, 11]
test_accuracies = []

for mf in features_list:
    rfr = RandomForestRegressor(n_estimators=25,
                                 random_state=1111,
                                 max_features=mf)
    rfr.fit(X_train, y_train)
    test_mae = mae(y_test, rfr.predict(X_test))
    test_accuracies.append(test_mae)

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(features_list, test_accuracies, marker='o')
plt.title('Test Data Accuracy by Number of Features')
plt.xlabel('Number of Features')
plt.ylabel('Test Set Accuracy')
plt.xticks(features_list, ['2 Features\n(underfit)', '4 Features', '11 Features\n(overfit)'])
plt.grid(True)
plt.show()