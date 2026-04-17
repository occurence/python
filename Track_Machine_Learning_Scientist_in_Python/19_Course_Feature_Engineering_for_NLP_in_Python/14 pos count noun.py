import spacy

nlp = spacy.load('en_core_web_sm')

# Returns number of other nouns
def nouns(text, model=nlp):
  	# Create doc object
    doc = model(text)
    # Generate list of POS tags
    pos = [token.pos_ for token in doc]
    
    # Return number of other nouns
    return pos.count('NOUN')

print(nouns("Abdul, Bill and Cathy went to the market to buy apples.", nlp))

print("You now know how to write functions that compute the number of instances of a particulat POS tag in a given piece of text. In the next exercise, we will use these functions to generate features from text in a dataframe.")