import spacy
from spacy.training import Example
import random

nlp = spacy.load("en_core_web_sm")
test = "I'm going to Sam's house."
training_data = [('I will visit you in Austin.', {'entities': [(20, 26, 'GPE')]}),
                ("I'm going to Sam's house.",
                {'entities': [(13, 16, 'PERSON'), (19, 24, 'GPE')]}),
                ('I will go.', {'entities': []})]
epochs = 2

nlp = spacy.load("en_core_web_sm")
print("Before training: ", [(ent.text, ent.label_) for ent in nlp(test).ents])
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
nlp.disable_pipes(*other_pipes)
optimizer = nlp.create_optimizer()

# Shuffle training data and the dataset using random package per epoch
for i in range(epochs):
  random.shuffle(training_data)
  for text, annotations in training_data:
    doc = nlp.make_doc(text)
    # Update nlp model after setting sgd argument to optimizer
    example = Example.from_dict(doc, annotations)
    nlp.update([example], sgd = optimizer)
print("After training: ", [(ent.text, ent.label_) for ent in nlp(test).ents])

print("You just trained an existing spaCy NER model for two epochs. You can see that prior to training, the model was unable to predict house as an entity, but training helped with model predictions.")