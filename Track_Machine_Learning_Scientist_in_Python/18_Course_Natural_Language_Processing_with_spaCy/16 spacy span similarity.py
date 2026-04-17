import spacy

nlp = spacy.load('en_core_web_md')
texts = 'canned food products.'
document = nlp(texts)

# Create a Doc container for the category
category = "canned dog food"
category_document = nlp(category)

# Print similarity score of a given Span and category_document
document_span = document[0:3]
print(f"Semantic similarity with", document_span.text, ":", round(document_span.similarity(category_document), 3))