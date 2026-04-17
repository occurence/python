import spacy

nlp = spacy.load('en_core_web_md')
token = nlp("computer")[0]

# Initialize best similarity
max_sim = -1
most_similar = ""

# Compare with all tokens in vocab
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