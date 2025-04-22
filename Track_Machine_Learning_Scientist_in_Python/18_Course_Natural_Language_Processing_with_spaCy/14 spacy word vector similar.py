import spacy
import numpy as np

nlp = spacy.load('en_core_web_md')

# Find the most similar word to the word computer
most_similar_words = nlp.vocab.vectors.most_similar(np.asarray([nlp.vocab.vectors[nlp.vocab.strings['computer']]]), n = 1)

# Find the list of similar words given the word IDs
words = [nlp.vocab.strings[w] for w in most_similar_words[0][0]]
print(words)

token = nlp("computer")[0]
max_sim = -1
most_similar = ""

for word in nlp.vocab:
    if word.has_vector and word.is_lower and word.is_alpha:
        similarity = token.similarity(word)
        if similarity > max_sim and word.text != token.text:
            max_sim = similarity
            most_similar = word.text

print([most_similar])

print("computer-related" in nlp.vocab)
print(nlp.vocab["computer-related"].has_vector)

print("Similarity with 'space':", token.similarity(nlp.vocab["space"]))
print("Similarity with 'computer-related':", token.similarity(nlp.vocab["computer-related"]))