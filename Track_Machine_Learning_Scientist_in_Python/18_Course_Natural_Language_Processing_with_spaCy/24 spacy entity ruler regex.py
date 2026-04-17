import spacy

text = "Our phone number is 4251234567."

# Define a pattern to match phone numbers
patterns = [{"label": "PHONE_NUMBERS", "pattern": [{"TEXT": {"REGEX": "(\d){10}"}}]}]

# Load a blank model and add an EntityRuler
nlp = spacy.blank("en")
ruler = nlp.add_pipe("entity_ruler")

# Add the compiled patterns to the EntityRuler
ruler.add_patterns(patterns)

# Print the tuple of entities texts and types for the given text
doc = nlp(text)
print([(ent.text, ent.label_) for ent in doc.ents])

print("You are now able to write a regular expression pattern and use spaCy EntityRuler to align the matched patterns with a given Doc container entities.")