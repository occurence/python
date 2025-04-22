import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')
text = 'I have bought several of the Vitality canned dog food products and have found them all to be of good quality. The product looks more like a stew than a processed meat and it smells better. My Labrador is finicky and she appreciates this product better than  most.'

# Create a Doc container of the given text
document = nlp(text)

# Store and review the token text values of tokens for the Doc container
first_text_tokens = [token.text for token in document]
print("First text tokens:\n", first_text_tokens, "\n")

# displacy.serve(document, style='ent')
displacy.serve(document, style='dep')