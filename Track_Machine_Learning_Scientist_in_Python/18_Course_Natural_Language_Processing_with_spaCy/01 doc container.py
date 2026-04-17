import spacy

text = 'NLP is becoming increasingly popular for providing business solutions.'

# Load en_core_web_sm and create an nlp object
nlp = spacy.load('en_core_web_sm')

# Create a Doc container for the text object
doc = nlp(text)

# Create a list containing the text of each token in the Doc container
print([token.text for token in doc])