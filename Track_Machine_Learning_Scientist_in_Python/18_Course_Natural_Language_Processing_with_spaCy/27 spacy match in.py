import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
example_text = 'It is cut into tiny squares and then liberally coated with powdered sugar.  And it is a tiny mouthful of heaven.'
doc = nlp(example_text)

# Define a matcher object
matcher = Matcher(nlp.vocab)
# Define a pattern to match tiny squares and tiny mouthful
pattern = [{"lower": "tiny"}, {"lower": {"IN": ["squares", "mouthful"]}}]

# Add the pattern to matcher object and find matches
matcher.add("CustomMatcher", [pattern])
matches = matcher(doc)

# Print out start and end token indices and the matched text span per match
for match_id, start, end in matches:
    print("Start token: ", start, " | End token: ", end, "| Matched text: ", doc[start:end].text)