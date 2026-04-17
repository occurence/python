import pandas as pd

movie = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\09_Course_Cluster_Analysis_in_Python\datasets\movies_plot.csv')
stop_words_2 = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\09_Course_Cluster_Analysis_in_Python\datasets\stop_words_2.csv', header=None)
plots = movie['Plot'].tolist()
stop_words_2 = stop_words_2[0].tolist()

from nltk.tokenize import word_tokenize
import re

def remove_noise(text, stop_words = stop_words_2):
    tokens = word_tokenize(text)
    cleaned_tokens = []
    for token in tokens:
        token = re.sub('[^A-Za-z0-9]+', '', token)
        if len(token) > 1 and token.lower() not in stop_words:
            # Get lowercase
            cleaned_tokens.append(token.lower())
    return cleaned_tokens


# Import TfidfVectorizer class from sklearn
from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(min_df=0.1, max_df=0.75, max_features=50, tokenizer=remove_noise)

# Use the .fit_transform() method on the list plots
tfidf_matrix = tfidf_vectorizer.fit_transform(plots)