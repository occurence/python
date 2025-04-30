import spacy

nlp = spacy.load('en_core_web_lg')
sent = 'I like apples and oranges'

# Create the doc object
doc = nlp(sent)

# Compute pairwise similarity scores
for token1 in doc:
  for token2 in doc:
    print(token1.text, token2.text, token1.similarity(token2))

print("Notice how the words 'apples' and 'oranges' have the highest pairwaise similarity score. This is expected as they are both fruits and are more related to each other than any other pair of words.")