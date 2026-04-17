import spacy

nlp = spacy.load('en_core_web_md')
words = ["like", "love"]

# IDs of all the given words
ids = [nlp.vocab.strings[w] for w in words]

# Store the first ten elements of the word vectors for each word
word_vectors = [nlp.vocab.vectors[i][:10] for i in ids]

# Print the first ten elements of the first word vector
print(word_vectors[0])