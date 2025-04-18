from gensim.utils import simple_preprocess

articles = open(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\17_Course_Introduction_to_Natural_Language_Processing\datasets\wiki_text_software.txt', 'r', encoding='utf-8').read()
# articles = list(articles)
# articles = set(articles.splitlines())
# print(repr(articles))
articles = articles.split('\n')
articles = [doc.split() for doc in articles if doc.strip() != ""]
# articles = [simple_preprocess(doc) for doc in articles.split('\n') if doc.strip() != ""]
# articles = [simple_preprocess(doc) for doc in articles.split('\n') if doc.strip()]
# articles = [doc.lower().split() for doc in articles.split('\n') if doc.strip()]
# articles = [doc.split() for doc in articles.split('\n') if doc.strip()]
# articles = [doc.lower().split() for doc in articles.split('\n') if doc.strip()]

# print(articles)

# Import Dictionary
from gensim.corpora.dictionary import Dictionary

# Create a Dictionary from the articles: dictionary
dictionary = Dictionary(articles)

# Select the id for "computer": computer_id
computer_id = dictionary.token2id.get("computer")

# Use computer_id with the dictionary to print the word
print(dictionary.get(computer_id))

# Create a MmCorpus: corpus
corpus = [dictionary.doc2bow(article) for article in articles]

# Print the first 10 word ids with their frequency counts from the fifth document
print(corpus[4][:10])

for word_id, count in corpus[4][:10]:
    print(f"{dictionary[word_id]}: {count}")
