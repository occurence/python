import pandas as pd
import spacy
from spacy.training import Example
import random

df = pd.read_json(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\18_Course_Natural_Language_Processing_with_spaCy\datasets\corona.json')
training_data = [(row[0], row[1]) for row in df.itertuples(index=False)]
labels = ['Pathogen', 'MedicalCondition', 'Medicine']

# Load a blank English model, add NER component, add given labels to the ner pipeline
nlp = spacy.blank("en")
ner = nlp.add_pipe("ner")
for ent in labels:
    ner.add_label(ent)

# Disable other pipeline components, complete training loop and run training loop
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
nlp.disable_pipes(*other_pipes)
losses = {}
optimizer = nlp.begin_training()
for text, annotation in training_data:
    doc = nlp.make_doc(text)
    example = Example.from_dict(doc, annotation)
    nlp.update([example], sgd=optimizer, losses=losses)
    print(losses)