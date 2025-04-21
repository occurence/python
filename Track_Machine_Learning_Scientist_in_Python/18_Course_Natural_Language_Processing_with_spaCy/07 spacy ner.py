import spacy

nlp = spacy.load('en_core_web_sm')

texts = ['I want to fly from Boston at 8:38 am and arrive in Denver at 11:10 in the morning',
 'What flights are available from Pittsburgh to Baltimore on Thursday morning?',
 'What is the arrival time in San francisco for the 7:55 AM flight leaving Washington?']

# Compile a list of all Doc containers of texts
documents = [nlp(text) for text in texts]

# Print the entity text and label for the entities in each document
for doc in documents:
    print([(ent.text, ent.label_) for ent in doc.ents])
    
# Print the 6th token's text and entity type of the second document
print("\nText:", documents[1][5].text, "| Entity type: ", documents[1][5].ent_type_)