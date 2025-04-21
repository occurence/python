import nltk
nltk.download('punkt')

sentence = "Polyglot is an interesting library for NLP."
words = nltk.word_tokenize(sentence)
print("Tokenized words:", words)
