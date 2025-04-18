import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from gensim.corpora.dictionary import Dictionary
import itertools
from collections import defaultdict

articles = open(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\17_Course_Introduction_to_Natural_Language_Processing\datasets\wiki_text_software.txt', 'r', encoding='utf-8').read()
'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\17_Course_Introduction_to_Natural_Language_Processing\datasets\wiki_text_debugging.txt'
'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\17_Course_Introduction_to_Natural_Language_Processing\datasets\wiki_text_crash.txt'
'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\17_Course_Introduction_to_Natural_Language_Processing\datasets\wiki_text_malware.txt'
'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\17_Course_Introduction_to_Natural_Language_Processing\datasets\wiki_text_reversing.txt'
'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\17_Course_Introduction_to_Natural_Language_Processing\datasets\wiki_text_hopper.txt'
'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\17_Course_Introduction_to_Natural_Language_Processing\datasets\wiki_text_computer.txt'
'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\17_Course_Introduction_to_Natural_Language_Processing\datasets\wiki_text_program.txt'
'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\17_Course_Introduction_to_Natural_Language_Processing\datasets\wiki_text_bug.txt'
'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\17_Course_Introduction_to_Natural_Language_Processing\datasets\wiki_text_debugger.txt'
'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\17_Course_Introduction_to_Natural_Language_Processing\datasets\wiki_text_exception.txt'
'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\17_Course_Introduction_to_Natural_Language_Processing\datasets\wiki_text_language.txt'
# print(repr(articles.read()))

from collections import Counter
tokens = word_tokenize(articles)
lower_tokens = [t.lower() for t in tokens]
bow_simple = Counter(lower_tokens)
print(bow_simple.most_common(10))
# print(lower_tokens)

english_stops = open(r'Track_Machine_Learning_Scientist_in_Python/17_Course_Introduction_to_Natural_Language_Processing/datasets/english_stopwords.txt', 'r', encoding='utf-8').read()
english_stops = set(english_stops.splitlines())

alpha_only = [t for t in word_tokenize(articles.lower()) if t.isalpha()]
no_stops = [t for t in alpha_only if t not in english_stops]
wordnet_lemmatizer = WordNetLemmatizer()
lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]
bow = Counter(lemmatized)
print(bow.most_common(10))
# print(bow)

print("DICTIONARY")
articles = articles.split('\n')
articles = [doc.split() for doc in articles if doc.strip() != ""]
# articles = [t for t in lower_tokens if t.isalpha()]
# articles = [t for t in alpha_only if t not in english_stops]
filtered_tokens = [t for t in lower_tokens if any(c.isalnum() for c in t)]
articles = [t for t in filtered_tokens if t not in english_stops]
print(articles)

# dictionary = Dictionary(articles)
# computer_id = dictionary.token2id.get("computer")
# print(dictionary.get(computer_id))
# corpus = [dictionary.doc2bow(article) for article in articles]
# print(corpus[4][:10])
# for word_id, count in corpus[4][:10]:
#     print(f"{dictionary[word_id]}: {count}")

# print("GENSIM")
# # Save the fifth document: doc
# doc = corpus[4]

# # Sort the doc for frequency: bow_doc
# bow_doc = sorted(doc, key=lambda w: w[1], reverse=True)

# # Print the top 5 words of the document alongside the count
# for word_id, word_count in bow_doc[:5]:
#     print(dictionary.get(word_id), word_count)
    
# # Create the defaultdict: total_word_count
# total_word_count = defaultdict(int)
# for word_id, word_count in itertools.chain.from_iterable(corpus):
#     total_word_count[word_id] += word_count
    
# # Create a sorted list from the defaultdict: sorted_word_count
# sorted_word_count = sorted(total_word_count.items(), key=lambda w: w[1], reverse=True) 

# # Print the top 5 words across all documents alongside the count
# for word_id, word_count in sorted_word_count[:5]:
#     print(dictionary.get(word_id), word_count)