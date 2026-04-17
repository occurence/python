import spacy
from spacy.training import Example

nlp = spacy.load("en_core_web_sm")
text = 'I will visit you in Austin.'
annotations = {'entities': [(20, 26, 'GPE')]}

# Disable all pipeline components of  except `ner`
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
nlp.disable_pipes(*other_pipes)

# Convert a text and its annotations to the correct format usable for training
doc = nlp.make_doc(text)
example = Example.from_dict(doc, annotations)
print("Example object for training: \n", example.to_dict())

print("You can now disbale pipeline components and convert data into proper spaCy format for training, an Example class with multiple keys such as entities and token_annotations.")