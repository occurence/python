import pandas as pd
from sklearn.model_selection import train_test_split

reviews = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\19_Course_Feature_Engineering_for_NLP_in_Python\datasets\movie_reviews_clean.csv')
index = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\19_Course_Feature_Engineering_for_NLP_in_Python\datasets\train_250.csv', header=None, index_col=0)
X = reviews.drop("sentiment", axis=1)
y = reviews["sentiment"].values

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.75, random_state=631)
X_train = reviews.iloc[index.index]['review']
X_test = reviews.drop(index.index)['review']
y_train = reviews.iloc[index.index]['sentiment']
y_test = reviews.drop(index.index)['sentiment']

# Import CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer

# Create a CountVectorizer object
vectorizer = CountVectorizer(lowercase=True, stop_words='english')

# Fit and transform X_train
X_train_bow = vectorizer.fit_transform(X_train)

# Transform X_test
X_test_bow = vectorizer.transform(X_test)

# Print shape of X_train_bow and X_test_bow
print(X_train_bow.shape)
print(X_test_bow.shape)

print("You now have a good idea of preprocessing text and transforming them into their bag-of-words representation using CountVectorizer. In this exercise, you have set the lowercase argument to True. However, note that this is the default value of lowercase and passing it explicitly is not necessary. Also, note that both X_train_bow and X_test_bow have 8158 features. There were words present in X_test that were not in X_train. CountVectorizer chose to ignore them in order to ensure that the dimensions of both sets remain the same.")