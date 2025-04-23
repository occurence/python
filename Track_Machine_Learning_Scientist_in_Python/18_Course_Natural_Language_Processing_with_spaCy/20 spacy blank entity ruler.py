import spacy

nlp = spacy.blank("en")
patterns = [{"label": "ORG", "pattern": [{"LOWER": "openai"}]},
            {"label": "ORG", "pattern": [{"LOWER": "microsoft"}]}]
text = "OpenAI has joined forces with Microsoft."

# Add EntityRuler component to the model
entity_ruler = nlp.add_pipe("entity_ruler")

# Add given patterns to the EntityRuler component
entity_ruler.add_patterns(patterns)

# Run the model on a given text
doc = nlp(text)

# Print entities text and type for all entities in the Doc container
print([(ent.text, ent.label_) for ent in doc.ents])

print("You can now define as many patterns and use EntityRuler to perform purely rule-based entity recognition for a given text. In this instance, OpenAI and Microsoft are identified correctly as ORG (organization).")