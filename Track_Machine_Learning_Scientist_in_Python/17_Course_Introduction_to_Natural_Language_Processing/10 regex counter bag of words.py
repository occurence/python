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

print(lower_tokens)