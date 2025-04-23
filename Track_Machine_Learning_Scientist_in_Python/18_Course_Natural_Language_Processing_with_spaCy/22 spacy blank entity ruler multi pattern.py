import spacy

nlp = spacy.load("en_core_web_md")
example_text = 'This is a confection. In this case Filberts. And it is cut into tiny squares. This is the treat that seduces Edmund into selling out his Brother and Sisters to the Witch.'

# Print a list of tuples of entities text and types in the example_text
print("Before EntityRuler: ", [ent.text for ent in nlp(example_text).ents], "\n")

# Define pattern to add a label PERSON for lower cased sisters and brother entities
patterns = [{"label": "PERSON", "pattern": [{"lower": "brother"}]},
            {"label": "PERSON", "pattern": [{"lower": "sisters"}]}]

# Add an EntityRuler component and add the patterns to the ruler
ruler = nlp.add_pipe("entity_ruler")
ruler.add_patterns(patterns)

# Print a list of tuples of entities text and types
print("After EntityRuler: ", [(ent.text, ent.label_) for ent in nlp(example_text).ents])

print("Now you are able to handcraft rules in spaCy using EntityRuler and ensure spaCy models are able to correctly identify entities and their corresponding labels. In this instance, the EntityRuler helps to predict brother and sisters correctly as PERSON.")