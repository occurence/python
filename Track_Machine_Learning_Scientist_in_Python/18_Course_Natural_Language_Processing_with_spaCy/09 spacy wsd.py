import spacy

nlp = spacy.load('en_core_web_sm')
texts = ["This device is used to jam the signal.",
         "I am stuck in a traffic jam"]

# Create a list of Doc containers in the texts list
documents = [nlp(t) for t in texts]

# Print a token's text and POS tag if the word jam is in the token's text
for i, doc in enumerate(documents):
    print(f"Sentence {i+1}: ", [(token.text, token.pos_) for token in doc if "jam" in token.text], "\n")