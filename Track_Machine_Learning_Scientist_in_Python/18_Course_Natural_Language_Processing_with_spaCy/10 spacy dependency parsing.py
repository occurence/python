import spacy

nlp = spacy.load('en_core_web_sm')
texts = ['I want to fly from Boston at 8:38 am and arrive in Denver at 11:10 in the morning',
 'What flights are available from Pittsburgh to Baltimore on Thursday morning?',
 'What is the arrival time in San francisco for the 7:55 AM flight leaving Washington?']

# Create a list of Doc containts of texts list
documents = [nlp(t) for t in texts]

# Print each token's text, dependency label and its explanation
for doc in documents:
    print([(token.text, token.dep_, spacy.explain(token.dep_)) for token in doc], "\n")