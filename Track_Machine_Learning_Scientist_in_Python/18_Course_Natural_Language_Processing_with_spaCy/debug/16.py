import spacy

nlp = spacy.load("en_core_web_md")
token = nlp("computer")[0]

# Manually add custom candidates
candidates = ["computer-related"]
for word in nlp.vocab:
    if word.has_vector and word.is_lower and word.is_alpha:
        candidates.append(word.text)

# Compare similarities
max_sim = -1
most_similar = ""
for word in candidates:
    word_token = nlp.vocab[word]
    if word_token.has_vector and word_token.text != token.text:
        similarity = token.similarity(word_token)
        if similarity > max_sim:
            max_sim = similarity
            most_similar = word_token.text

print([most_similar])

print("Similarity with 'space':", token.similarity(nlp.vocab["space"]))
print("Similarity with 'computer-related':", token.similarity(nlp.vocab["computer-related"]))
