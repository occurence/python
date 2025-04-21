import spacy

nlp = spacy.load('en_core_web_sm')

texts = ['What is the arrival time in San francisco for the 7:55 AM flight leaving Washington?',
 'Cheapest airfare from Tacoma to Orlando is 650 dollars.',
 'Round trip fares from Pittsburgh to Philadelphia are under 1000 dollars!']

# Compile a list of all Doc containers of texts
documents = [nlp(text) for text in texts]

# Print token texts and POS tags for each Doc container
for doc in documents:
    for token in doc:
        print("Text: ", token.text, "| POS tag: ", token.pos_)
    print("\n")