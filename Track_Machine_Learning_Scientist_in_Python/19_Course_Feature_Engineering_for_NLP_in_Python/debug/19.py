import pandas as pd
import spacy

nlp = spacy.load('en_core_web_md')
movie = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\19_Course_Feature_Engineering_for_NLP_in_Python\datasets\movie_overviews.csv')
stopwords = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\19_Course_Feature_Engineering_for_NLP_in_Python\datasets\stopwords.csv', header=None).values.flatten().tolist()
movie = movie.dropna()
# print(movie.loc[7333:7353, 'tagline'])
def preprocess(text):
    doc = nlp(text.lower(), disable=['ner'])
    lemmas = [token.lemma_ for token in doc]
    a_lemmas = [lemma for lemma in lemmas 
            if lemma.isalpha() and lemma not in stopwords]
    return ' '.join(a_lemmas)

lem_corpus = movie['tagline'].apply(preprocess)
# lem_corpus = lem_corpus.dropna()
lem_corpus = lem_corpus[lem_corpus != '']
# print(lem_corpus)
# print(lem_corpus.iloc[5666])

# print(lem_corpus.isna())
# print(lem_corpus[lem_corpus.isna()])
# print(lem_corpus.iloc[-20:])


# for elem in lem_corpus:
#     print(f"{len(elem)}")

# print(lem_corpus.apply(len))

# lem_corpus.to_csv('lem_corpus.csv', index=False)



# Import CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer

# Create CountVectorizer object
vectorizer = CountVectorizer()

# Generate matrix of word vectors
bow_lem_matrix = vectorizer.fit_transform(lem_corpus)

# Print the shape of bow_lem_matrix
print(bow_lem_matrix.shape)