import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
example_text = 'I highly recommend this yummy treat.  If you are familiar with the story of C.S. Lewis\' "The Lion, The Witch, and The Wardrobe" - this is the treat that seduces Edmund into selling out his Brother and Sisters to the Witch.'
doc = nlp(example_text)

# Initialize a Matcher object
matcher = Matcher(nlp.vocab)

# Define a pattern to match lower cased word witch
pattern = [{"lower" : "witch"}]

# Add the pattern to matcher object and find matches
matcher.add("CustomMatcher", [pattern])
matches = matcher(doc)

# Print start and end token indices and span of the matched text
for match_id, start, end in matches:
    print("Start token: ", start, " | End token: ", end, "| Matched text: ", doc[start:end].text)

print("Matcher is one of the commonly used functionalities in spaCy to find given patterns in a text. In this case, you identify two occurrences of the word witch in the given context.")