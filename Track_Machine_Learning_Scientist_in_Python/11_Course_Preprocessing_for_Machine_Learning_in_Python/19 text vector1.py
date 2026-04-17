import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.feature_extraction.text import TfidfVectorizer

volunteer_dense = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\11_Course_Preprocessing_for_Machine_Learning_in_Python\datasets\volunteer_sparse.csv')
volunteer = csr_matrix((volunteer_dense['value'], (volunteer_dense['row'], volunteer_dense['col'])))

vocab = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\11_Course_Preprocessing_for_Machine_Learning_in_Python\datasets\vocab.csv')
vocab = dict(zip(vocab['keys'], vocab['values']))

text_tfidf_dense = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\11_Course_Preprocessing_for_Machine_Learning_in_Python\datasets\text_tfidf.csv')
text_tfidf = csr_matrix((text_tfidf_dense['value'], (text_tfidf_dense['row'], text_tfidf_dense['col'])))

tfidf_vec = TfidfVectorizer()
tfidf_matrix = tfidf_vec.fit_transform(list(vocab.values()))

# Add in the rest of the arguments
def return_weights(vocab, original_vocab, vector, vector_index, top_n):
    zipped = dict(zip(vector[vector_index].indices, vector[vector_index].data))
    
    # Transform that zipped dict into a series
    zipped_series = pd.Series({vocab[i]:zipped[i] for i in vector[vector_index].indices})
    
    # Sort the series to pull out the top n weighted words
    zipped_index = zipped_series.sort_values(ascending=False)[:top_n].index
    return [original_vocab[i] for i in zipped_index]
    

# Print out the weighted words
print(return_weights(vocab, original_vocab=tfidf_vec.vocabulary_, vector=text_tfidf, vector_index=8, top_n=3))

def word_weights(vocab, vector, vector_index):
    zipped = dict(zip(vector[vector_index].indices, vector[vector_index].data))
    return {vocab[i]:zipped[i] for i in vector[vector_index].indices}

print(word_weights(vocab, text_tfidf, 8))