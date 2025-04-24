import spacy

nlp = spacy.load("en_core_web_sm")
texts = ['Product arrived labeled as Jumbo Salted Peanuts.',
 'Not sure if the product was labeled as Jumbo.']
documents = [nlp(t) for t in texts]

# Append a tuple of (entities text, entities label) if Jumbo is in the entity
target_entities = []
for doc in documents:
  target_entities.extend([(ent.text, ent.label_) for ent in doc.ents if "Jumbo" in ent.text])
print(target_entities)

# Append True to the correct_labels list if the entity label is `PRODUCT`
correct_labels = []
for ent in target_entities:
  if ent[1] == "PRODUCT":
    correct_labels.append(True)
  else:
    correct_labels.append(False)
print(correct_labels)

print("You can observe that none of the Jumbo entities are correctly classified as PRODUCT. This shows that the current spaCy model needs to be trained further to classify PRODUCT entities better.")