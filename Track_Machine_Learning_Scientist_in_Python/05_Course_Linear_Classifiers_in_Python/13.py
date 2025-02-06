import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.linear_model import LogisticRegression

# Load vocabulary and training data
vocab = np.array(pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\vocab.csv'))
df_X_train = pd.read_csv(r"D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\sentiment_X_train.csv")
X_train = csr_matrix((df_X_train['value'], (df_X_train['row'], df_X_train['col'])), shape=(5000, 2500))  # Replace with actual shape
y_train = np.array(pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\sentiment_y_train.csv', header=None))

# Initialize logistic regression model
lr = LogisticRegression(solver='liblinear')

# Fit the model
lr.fit(X_train, y_train.ravel())

# Get the indices of the sorted coefficients
inds_ascending = np.argsort(lr.coef_.flatten())
inds_descending = inds_ascending[::-1]

# Print the most positive words
print("Most positive words: ", end="")
for i in range(5):
    print(vocab[inds_descending[i]], end=", ")
print("\n")

# Print most negative words
print("Most negative words: ", end="")
for i in range(5):
    print(vocab[inds_ascending[i]], end=", ")
print("\n")
