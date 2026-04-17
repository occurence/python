print("Starting script...")
from polyglot.text import Text
print("Polyglot loaded.")
text = Text("Polyglot is amazing!")
print("Text processed.")
print("Language detected:", text.language)
print("Sentiment:", text.sentiment)
