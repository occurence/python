import pandas as pd

ted = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\19_Course_Feature_Engineering_for_NLP_in_Python\datasets\ted.csv')
ted = ted['transcript']

# Import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Create TfidfVectorizer object
vectorizer = TfidfVectorizer()

# Generate matrix of word vectors
tfidf_matrix = vectorizer.fit_transform(ted)

# Print the shape of tfidf_matrix
print(tfidf_matrix.shape)

print("You now know how to generate tf-idf vectors for a given corpus of text. You can use these vectors to perform predictive modeling just like we did with CountVectorizer. In the next few lessons, we will see another extremely useful application of the vectorized form of documents: generating recommendations.")