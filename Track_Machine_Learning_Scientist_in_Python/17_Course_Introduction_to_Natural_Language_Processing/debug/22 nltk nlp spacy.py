import os
import nltk
import spacy
import matplotlib.pyplot as plt
from collections import defaultdict

# Optional: Custom NLTK data path (portable projects)
# nltk_data_dir = os.path.join(os.getcwd(), 'nltk_data')
# nltk.data.path.append(nltk_data_dir)

# Automatically download required NLTK resources
nltk.download('punkt')  # For sentence and word tokenization
nltk.download('averaged_perceptron_tagger')  # POS tagging
nltk.download('maxent_ne_chunker')  # Named entity chunker
nltk.download('words')  # Word lists for NE
# nltk.download('popular')  # (Optional: download all major resources)

# Load spaCy model (download if not available)
try:
    nlp = spacy.load('en_core_web_sm', disable=['tagger', 'parser', 'matcher'])
except:
    spacy.cli.download('en_core_web_sm')
    nlp = spacy.load('en_core_web_sm', disable=['tagger', 'parser', 'matcher'])

# === Load article ===
file_path = r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\17_Course_Introduction_to_Natural_Language_Processing\datasets\articles.txt'
with open(file_path, 'r', encoding='utf-8') as f:
    article = f.read()

# === NLTK Pipeline ===
print("\n🔍 NLTK Named Entities:")

# Tokenize into sentences, then words, then POS tag
sentences = nltk.sent_tokenize(article)
token_sentences = [nltk.word_tokenize(sent) for sent in sentences]
pos_sentences = [nltk.pos_tag(sent) for sent in token_sentences]

# Named Entity Chunking
chunked_sentences = list(nltk.ne_chunk_sents(pos_sentences, binary=False))

# Count Named Entities
nltk_ner_counts = defaultdict(int)

for sent in chunked_sentences:
    for chunk in sent:
        if hasattr(chunk, 'label'):
            print(f"{chunk.label()}: {' '.join(c[0] for c in chunk)}")
            nltk_ner_counts[chunk.label()] += 1

# Plot NLTK NER Results
if nltk_ner_counts:
    plt.figure(figsize=(6,6))
    plt.title("NLTK Named Entity Recognition")
    plt.pie(
        list(nltk_ner_counts.values()),
        labels=list(nltk_ner_counts.keys()),
        autopct='%1.1f%%',
        startangle=140
    )
    plt.axis('equal')
    plt.show()
else:
    print("No named entities found with NLTK.")

# === spaCy Pipeline ===
print("\n🔍 spaCy Named Entities:")
doc = nlp(article)

spacy_ner_counts = defaultdict(int)
for ent in doc.ents:
    print(f"{ent.label_}: {ent.text}")
    spacy_ner_counts[ent.label_] += 1

# Plot spaCy NER Results
if spacy_ner_counts:
    plt.figure(figsize=(6,6))
    plt.title("spaCy Named Entity Recognition")
    plt.pie(
        list(spacy_ner_counts.values()),
        labels=list(spacy_ner_counts.keys()),
        autopct='%1.1f%%',
        startangle=140
    )
    plt.axis('equal')
    plt.show()
else:
    print("No named entities found with spaCy.")
