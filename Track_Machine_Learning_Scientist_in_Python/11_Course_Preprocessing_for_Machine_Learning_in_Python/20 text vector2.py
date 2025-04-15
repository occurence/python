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

def return_weights(vocab, original_vocab, vector, vector_index, top_n):
    zipped = dict(zip(vector[vector_index].indices, vector[vector_index].data))
    zipped_series = pd.Series({vocab[i]:zipped[i] for i in vector[vector_index].indices})
    zipped_index = zipped_series.sort_values(ascending=False)[:top_n].index
    return [original_vocab[i] for i in zipped_index]

print(return_weights(vocab, original_vocab=tfidf_vec.vocabulary_, vector=text_tfidf, vector_index=8, top_n=3))

def words_to_filter(vocab, original_vocab, vector, top_n):
    filter_list = []
    for i in range(0, vector.shape[0]):
    
        # Call the return_weights function and extend filter_list
        filtered = return_weights(vocab, original_vocab, vector, i, top_n)
        filter_list.extend(filtered)
        
    # Return the list in a set, so we don't get duplicate word indices
    return set(filter_list)

# Call the function to get the list of word indices
filtered_words = words_to_filter(vocab, original_vocab=tfidf_vec.vocabulary_, vector=text_tfidf, top_n=3)

# Filter the columns in text_tfidf to only those in filtered_words
filtered_text = text_tfidf[:, list(filtered_words)]

print(filtered_text)