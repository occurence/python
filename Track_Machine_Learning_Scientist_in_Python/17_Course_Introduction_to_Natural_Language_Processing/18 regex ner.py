import pandas as pd
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

article = open(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\17_Course_Introduction_to_Natural_Language_Processing\datasets\uber_apple.txt', 'r', encoding='utf-8').read()
article = repr(article)
# print(article)

# Tokenize the article into sentences: sentences
sentences = sent_tokenize(article)

# Tokenize each sentence into words: token_sentences
token_sentences = [nltk.word_tokenize(sent) for sent in sentences]

# Tag each tokenized sentence into parts of speech: pos_sentences
pos_sentences = [nltk.pos_tag(sent) for sent in token_sentences] 

# Create the named entity chunks: chunked_sentences
# chunked_sentences = nltk.ne_chunk_sents(pos_sentences, binary=True)
chunked_sentences = list(nltk.ne_chunk_sents(pos_sentences, binary=True))

# Test for stems of the tree with 'NE' tags
for sent in chunked_sentences:
    for chunk in sent:
        if hasattr(chunk, "label") and chunk.label() == "NE":
            print(chunk)

# for sent in list(chunked_sentences):
#     print(sent)

print(chunked_sentences)