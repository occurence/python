import spacy

texts = ['A loaded spaCy model can be used to compile documents list!',
         'Tokenization is the first step in any spacy pipeline.']

# Load en_core_web_sm model as nlp
nlp = spacy.load('en_core_web_sm')

# Run an nlp model on each item of texts and append the Doc container to documents
documents = []
for text in texts:
  documents.append(nlp(text))
  
# Print the token texts for each Doc container
for doc in documents:
  print([token.text for token in doc])