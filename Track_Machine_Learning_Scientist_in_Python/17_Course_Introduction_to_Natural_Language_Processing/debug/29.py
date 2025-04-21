from polyglot.text import Text

try:
    print("Script started")
    
    text = Text("Polyglot is amazing!")
    print("Text created")

    # Check language and sentiment
    print("Language detected:", text.language)
    print("Sentiment:", text.sentiment)

except Exception as e:
    print("An error occurred:", e)
