import spacy

# Load a blank spaCy English model
nlp = spacy.blank("en")

# Add tagger and entity_linker pipeline components
nlp.add_pipe("tagger")
nlp.add_pipe("entity_linker")

# Analyze the pipeline
analysis = nlp.analyze_pipes(pretty=True)

print("In this instance, the pipeline is missing sentence segmentation and named entity recognition components before entity_linker component!")