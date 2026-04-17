import spacy

nlp = spacy.load('en_core_web_md')
texts = 'This hot sauce is amazing! We picked up a bottle on a trip! '

# Populate Doc containers for the word "sauce" and for "texts" string
key = nlp('sauce')
sentences = nlp(texts)

# Calculate similarity score of each sentence and a Doc container for the word sauce
semantic_scores = []
for sent in sentences.sents:
	semantic_scores.append({"score": round(sent.similarity(key), 2)})
print(semantic_scores)