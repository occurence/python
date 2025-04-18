from nltk.tokenize import word_tokenize
from collections import Counter

text = 'The cat is in the box. The cat likes the box. The box is over the cat.'
# print(Counter(word_tokenize(text)).most_common(2))

tokens = word_tokenize(text)
counter = Counter(tokens)
print(counter.most_common(2))
print(counter)