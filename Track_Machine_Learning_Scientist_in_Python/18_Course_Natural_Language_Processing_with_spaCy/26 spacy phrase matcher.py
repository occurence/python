import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")
text = "There are only a few acceptable IP addresse: (1) 127.100.0.1, (2) 123.4.1.0."
terms = ["110.0.0.0", "101.243.0.0"]

# Initialize a PhraseMatcher class to match to shapes of given terms
matcher = PhraseMatcher(nlp.vocab, attr = "SHAPE")

# Create patterns to add to the PhraseMatcher object
patterns = [nlp.make_doc(term) for term in terms]
matcher.add("IPAddresses", patterns)

# Find matches to the given patterns and print start and end characters and matches texts
doc = nlp(text)
matches = matcher(nlp(text))
for match_id, start, end in matches:
    print("Start token: ", start, " | End token: ", end, "| Matched text: ", doc[start:end].text)

print("You can now find matches to a shape of given patterns using PhraseMatcher. In this instance, we identify two IP addresses that match the given shapes to the PhraseMatcher object.")