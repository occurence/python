import pandas as pd
from nltk.tokenize import word_tokenize

# with open(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\17_Course_Introduction_to_Natural_Language_Processing\datasets\wiki_text_debugging.txt', encoding='utf-8') as f:
#     article = f.read()
# print(repr(article))

article = open(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\17_Course_Introduction_to_Natural_Language_Processing\datasets\wiki_text_debugging.txt', 'r', encoding='utf-8').read()
# print(repr(article.read()))

# Import Counter
from collections import Counter

# Tokenize the article: tokens
tokens = word_tokenize(article)

# Convert the tokens into lowercase: lower_tokens
lower_tokens = [t.lower() for t in tokens]

# Create a Counter with the lowercase tokens: bow_simple
bow_simple = Counter(lower_tokens)

# Print the 10 most common tokens
print(bow_simple.most_common(10))

# print(lower_tokens)

english_stops = open(r'Track_Machine_Learning_Scientist_in_Python/17_Course_Introduction_to_Natural_Language_Processing/datasets/english_stopwords.txt', 'r', encoding='utf-8').read()
# english_stops = list(english_stops)
english_stops = set(english_stops.splitlines())
# print(type(english_stops))

# Import WordNetLemmatizer
from nltk.stem import WordNetLemmatizer

# Retain alphabetic words: alpha_only
alpha_only = [t for t in word_tokenize(article.lower()) if t.isalpha()]

# Remove all stop words: no_stops
no_stops = [t for t in alpha_only if t not in english_stops]

# Instantiate the WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

# Lemmatize all tokens into a new list: lemmatized
lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]

# Create the bag-of-words: bow
bow = Counter(lemmatized)

# Print the 10 most common tokens
print(bow.most_common(10))