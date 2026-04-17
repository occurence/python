import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

tictactoe = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\14_Course_Model_Validation_in_Python\datasets\tic-tac-toe.csv')

X = tictactoe.iloc[:, :-1]
y = tictactoe.iloc[:, -1]

ohe = OneHotEncoder(sparse_output=False)
X_enc = ohe.fit_transform(X).astype(int)
enc_columns = ohe.get_feature_names_out(X.columns)
X = pd.DataFrame(X_enc, columns=enc_columns)

le = LabelEncoder()
y = le.fit_transform(y).astype(int)

# Create two different samples of 200 observations 
sample1 = tictactoe.sample(200, random_state=1111)
sample2 = tictactoe.sample(200, random_state=1171)

# Print the number of common observations 
print(len([index for index in sample1.index if index in sample2.index]))

# Print the number of observations in the Class column for both samples 
print(sample1['Class'].value_counts())
print(sample2['Class'].value_counts())

print("Notice that there are a varying number of positive observations for both sample test sets. Sometimes creating a single test holdout sample is not enough to achieve the high levels of model validation you want. You need to use something more robust.")

print(X)