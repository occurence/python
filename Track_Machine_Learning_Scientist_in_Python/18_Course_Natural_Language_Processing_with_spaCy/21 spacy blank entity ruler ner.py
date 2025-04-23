import spacy

nlp = spacy.load("en_core_web_sm")
text = "New York Group was built in 1987."

# Add an EntityRuler to the nlp before NER component
ruler = nlp.add_pipe("entity_ruler", before="ner")

# Define a pattern to classify lower cased new york group as ORG
patterns = [{"label": "ORG", "pattern": [{"lower": "new york group"}]}]

# Add the patterns to the EntityRuler component
ruler.add_patterns(patterns)

# Run the model and print entities text and type for all the entities
doc = nlp(text)
print([(ent.text, ent.label_) for ent in doc.ents])

print("You just defined a token entity pattern and were able to improve the accuracy of an NER model by adding an EntityRuler before NER component of the spaCy model.")