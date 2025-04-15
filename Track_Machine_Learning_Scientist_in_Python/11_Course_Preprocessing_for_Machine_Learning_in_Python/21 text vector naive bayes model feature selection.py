import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.feature_extraction.text import TfidfVectorizer

volunteer_df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\11_Course_Preprocessing_for_Machine_Learning_in_Python\datasets\volunteer_opportunities.csv')
volunteer_df = volunteer_df.dropna(subset=['category_desc'])
y = volunteer_df["category_desc"]

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
        filtered = return_weights(vocab, original_vocab, vector, i, top_n)
        filter_list.extend(filtered)
    return set(filter_list)
filtered_words = words_to_filter(vocab, original_vocab=tfidf_vec.vocabulary_, vector=text_tfidf, top_n=3)
filtered_text = text_tfidf[:, list(filtered_words)]

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

nb = GaussianNB()

# Split the dataset according to the class distribution of category_desc
X_train, X_test, y_train, y_test = train_test_split(filtered_text.toarray(), y, stratify=y, random_state=42)

# Fit the model to the training data
nb.fit(X_train,y_train)

# Print out the model's accuracy
print(nb.score(X_test,y_test))