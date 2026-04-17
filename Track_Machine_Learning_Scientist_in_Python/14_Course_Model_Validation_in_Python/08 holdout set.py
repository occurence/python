import pandas as pd
from sklearn.model_selection import train_test_split

tictactoe = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\14_Course_Model_Validation_in_Python\datasets\tic-tac-toe.csv')

# Create dummy variables using pandas
X = pd.get_dummies(tictactoe.iloc[:,0:9], dtype=int)
y = tictactoe.iloc[:, 9]

# Create training and testing datasets. Use 10% for the test set
X_train, X_test, y_train, y_test  = train_test_split(X, y, test_size=0.1, random_state=1111)

print(y)