import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df_text = pd.read_csv(r"D:\STUDY\python\Track_Macine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\movie_X_train.csv")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df_text["review"])  # Now we fit it!

def get_features(review):
    return vectorizer.transform([review])



# df_X = pd.read_csv(r"D:\STUDY\python\Track_Macine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\movie_X_train.csv")
# X = csr_matrix((df_X['value'], (df_X['row'], df_X['col'])), shape=(2000, 2500))
# X = vectorizer.fit_transform(df_X["text"])
y = np.array(pd.read_csv(r'D:\STUDY\python\Track_Macine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\movie_y_train.csv', header=None))
# df_X_test = pd.read_csv(r"D:\STUDY\python\Track_Macine_Learning_Scientist_in_Python\05_Course_Linear_Classifiers_in_Python\datasets\movie_X_test.csv")
# X_test = csr_matrix((df_X_test['value'], (df_X_test['row'], df_X_test['col'])), shape=(2000, 2500))  # Replace with actual shape




# Instantiate logistic regression and train
# lr = LogisticRegression()
lr = LogisticRegression(max_iter=500)
# lr.fit(X, y)
lr.fit(X, y.ravel())

# Predict sentiment for a glowing review
review1 = "LOVED IT! This movie was amazing. Top 10 this year."
review1_features = get_features(review1)
print("Review:", review1)
print("Probability of positive review:", lr.predict_proba(review1_features)[0,1])

# Predict sentiment for a poor review
review2 = "Total junk! I'll never watch a film by that director again, no matter how good the reviews."
review2_features = get_features(review2)
print("Review:", review2)
print("Probability of positive review:", lr.predict_proba(review2_features)[0,1])