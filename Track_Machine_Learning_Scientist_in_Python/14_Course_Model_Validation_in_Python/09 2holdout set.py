import pandas as pd
from sklearn.model_selection import train_test_split

tictactoe = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\14_Course_Model_Validation_in_Python\datasets\tic-tac-toe.csv')

X = pd.get_dummies(tictactoe.iloc[:,0:9], dtype=int)
y = tictactoe.iloc[:, 9]

# Create temporary training and final testing datasets
X_temp, X_test, y_temp, y_test  =\
    train_test_split(X, y, test_size=0.2, random_state=1111)

# Create the final training and validation datasets
X_train, X_val, y_train, y_val =\
    train_test_split(X_temp, y_temp, test_size=0.25, random_state=1111)

print("You now have training, validation, and testing datasets, but do you know _when_ you need both validation and testing datasets? Keep going! The next exercise will help make sure you understand when to use validation datasets.")
print("Anytime we are evaluating model performance repeatedly we need to create training, validation, and testing datasets.")