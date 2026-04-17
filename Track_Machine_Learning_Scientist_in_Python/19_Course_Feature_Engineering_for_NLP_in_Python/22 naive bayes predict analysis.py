import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

reviews = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\19_Course_Feature_Engineering_for_NLP_in_Python\datasets\movie_reviews_clean.csv')
index = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\19_Course_Feature_Engineering_for_NLP_in_Python\datasets\train_250.csv', header=None, index_col=0)
X = reviews.drop("sentiment", axis=1)
y = reviews["sentiment"].values

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.75, random_state=631)
X_train = reviews.iloc[index.index]['review']
X_test = reviews.drop(index.index)['review']
y_train = reviews.iloc[index.index]['sentiment']
y_test = reviews.drop(index.index)['sentiment']

vectorizer = CountVectorizer(lowercase=True, stop_words='english')
X_train_bow = vectorizer.fit_transform(X_train)
X_test_bow = vectorizer.transform(X_test)
print(X_train_bow.shape)
print(X_test_bow.shape)

# Create a MultinomialNB object
clf = MultinomialNB()

# Fit the classifier
clf.fit(X_train_bow, y_train)

# Measure the accuracy
accuracy = clf.score(X_test_bow, y_test)
print("The accuracy of the classifier on the test set is %.3f" % accuracy)

# Predict the sentiment of a negative review
review = "The movie was terrible. The music was underwhelming and the acting mediocre."
prediction = clf.predict(vectorizer.transform([review]))[0]
print("The sentiment predicted by the classifier is %i" % (prediction))

print("You have successfully performed basic sentiment analysis. Note that the accuracy of the classifier is 73.2%. Considering the fact that it was trained on only 750 reviews, this is reasonably good performance. The classifier also correctly predicts the sentiment of a mini negative review which we passed into it.")