import spacy
import numpy as np
from sklearn.decomposition import PCA

nlp = spacy.load('en_core_web_md')
words = ["tiger", "bird"]

# Extract word IDs of given words
word_ids = [nlp.vocab.strings[w] for w in words]

# Extract word vectors and stack the first five elements vertically
word_vectors = np.vstack([nlp.vocab.vectors[i][:5] for i in word_ids])

# Calculate the transformed word vectors using the pca object
pca = PCA(n_components=2)
word_vectors_transformed = pca.fit_transform(word_vectors)

# Print the first component of the transformed word vectors
print(word_vectors_transformed[:, 0])