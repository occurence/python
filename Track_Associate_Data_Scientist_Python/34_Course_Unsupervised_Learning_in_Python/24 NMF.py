import pandas as pd
from scipy.sparse import csr_matrix

articles_dense = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\34_Course_Unsupervised_Learning_in_Python\datasets\articles.csv')
articles = csr_matrix((articles_dense['value'], (articles_dense['row'], articles_dense['col'])), shape=(60, 13125))

# Import NMF
from sklearn.decomposition import NMF

# Create an NMF instance: model
model = NMF(n_components=6)

# Fit the model to articles
model.fit(articles)

# Transform the articles: nmf_features
nmf_features = model.transform(articles)

# Print the NMF features
print(nmf_features.round(2))