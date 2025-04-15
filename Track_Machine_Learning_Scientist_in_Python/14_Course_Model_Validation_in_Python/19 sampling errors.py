import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error as mae
from sklearn.ensemble import RandomForestRegressor

candies = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\14_Course_Model_Validation_in_Python\datasets\candy-data.csv')
X = candies.iloc[:, 1:-1]
y = candies.iloc[:, -1]

s1 = candies.sample(60, random_state=1111)
s1_X = s1.iloc[:, 1:-1]
s1_y = s1.iloc[:, -1]
s1_X_temp, s1_X_test, s1_y_temp, s1_y_test  = train_test_split(s1_X, s1_y, test_size=0.2, random_state=1111)
s1_X_train, s1_X_val, s1_y_train, s1_y_val = train_test_split(s1_X_temp, s1_y_temp, test_size=0.25, random_state=1111)

s2 = candies.sample(60, random_state=1112)
s2_X = s2.iloc[:, 1:-1]
s2_y = s2.iloc[:, -1]
s2_X_temp, s2_X_test, s2_y_temp, s2_y_test  = train_test_split(s2_X, s2_y, test_size=0.2, random_state=1112)
s2_X_train, s2_X_val, s2_y_train, s2_y_val = train_test_split(s2_X_temp, s2_y_temp, test_size=0.25, random_state=1112)

print(len([i for i in s1.index if i in s2.index]))
print(s1.chocolate.value_counts())
print(s2.chocolate.value_counts())


X_temp, X_test, y_temp, y_test  = train_test_split(X, y, test_size=0.2, random_state=1171)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, random_state=1171)
rfr = RandomForestRegressor(n_estimators=25,
                            random_state=1111,
                            max_features=4)
rfr.fit(X_train, y_train)
print('Validation error {0:.2f}'.format(mae(y_test, rfr.predict(X_test))))
print('Testing error {0:.2f}'.format(mae(y_val, rfr.predict(X_val))))
# V     T       Seed
# 9.50  8.80    1111
# 12.99 6.88    1171


# print('S1 Testing error {0:.2f}'.format(mae(s1_y_test, rfr.predict(s1_X_test))))
# print('S2 Testing error {0:.2f}'.format(mae(s2_y_test, rfr.predict(s2_X_test))))