import spacy

nlp = spacy.load('en_core_web_md')
texts = ['I like the Vitality canned dog food products.',
 'The peanuts were actually small sized unsalted. Not sure if this was an error.',
 'It is a light, pillowy citrus gelatin with nuts - in this case Filberts.',
 'the Root Beer Extract I ordered is very medicinal.',
 'Great taffy at a great price.']

# Create a documents list containing Doc containers
documents = [nlp(t) for t in texts]

# Create a Doc container of the category
category = "canned dog food"
category_document = nlp(category)

# Print similarity scores of each Doc container and the category_document
for i, doc in enumerate(documents):
  print(f"Semantic similarity with document {i+1}:", round(doc.similarity(category_document), 3))