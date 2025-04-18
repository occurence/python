# Read the file
articles_raw = open(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\17_Course_Introduction_to_Natural_Language_Processing\datasets\wiki_text_software.txt', 'r', encoding='utf-8').read()

# Split into documents (e.g., by line)
documents = articles_raw.split('\n')
# documents = set(articles_raw.splitlines())
# documents = list(articles_raw)
print(documents)
# Tokenize each document (simple whitespace tokenization here)
articles = [doc.split() for doc in documents if doc.strip() != ""]

# Import Dictionary
from gensim.corpora.dictionary import Dictionary

# Create a Dictionary from the articles
dictionary = Dictionary(articles)

# Select the id for "computer"
computer_id = dictionary.token2id.get("computer")

# Use computer_id with the dictionary to print the word
print(dictionary.get(computer_id))

# Create a MmCorpus (bag-of-words for each document)
corpus = [dictionary.doc2bow(article) for article in articles]

# Print the first 10 word ids with their frequency counts from the fifth document
print(corpus[4][:10])
