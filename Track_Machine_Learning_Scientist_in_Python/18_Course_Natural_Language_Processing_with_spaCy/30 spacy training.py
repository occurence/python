import spacy
from spacy.training import Example

nlp = spacy.load("en_core_web_sm")
example_text = 'A patient with chest pain had hyperthyroidism.'
training_data = [(example_text, {'entities': [(15, 25, 'SYMPTOM'), (30, 45, 'DISEASE')]})]

all_examples = []
# Iterate through text and annotations and convert text to a Doc container
for text, annotations in training_data:
  doc = nlp(text)
  
  # Create an Example object from the doc contianer and annotations
  example_sentence = Example.from_dict(doc, annotations)
  print(example_sentence.to_dict(), "\n")
  
  # Append the Example object to the list of all examples
  all_examples.append(example_sentence)
  
print("Number of formatted training data: ", len(all_examples))

print("You can now convert training data into the proper object that is compatible for use during training of a spaCy model.")