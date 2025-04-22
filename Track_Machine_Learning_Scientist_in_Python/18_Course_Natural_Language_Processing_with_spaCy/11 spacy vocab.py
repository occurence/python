import spacy

# Load the en_core_web_md model
md_nlp = spacy.load('en_core_web_md')

# Print the number of words in the model's vocabulary
print("Number of words: ", md_nlp.meta["vectors"]["vectors"], "\n")

# Print the dimensions of word vectors in en_core_web_md model
print("Dimension of word vectors: ", md_nlp.meta["vectors"]["width"])