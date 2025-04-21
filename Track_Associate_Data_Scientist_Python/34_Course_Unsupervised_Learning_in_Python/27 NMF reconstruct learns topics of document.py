import pandas as pd
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer

words_df = pd.read_table(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\34_Course_Unsupervised_Learning_in_Python\datasets\wikipedia-vocabulary-utf8.txt', header=None, names=['word'],encoding='utf-8')
words_df = words_df.dropna()
words = words_df['word'].tolist()
tfidf = TfidfVectorizer()
csr_mat = tfidf.fit_transform(words)
model = NMF(n_components=6)
nmf_features = model.fit_transform(csr_mat)
words = tfidf.get_feature_names_out()

# Import pandas
import pandas as pd

# Create a DataFrame: components_df
components_df = pd.DataFrame(model.components_, columns=words)

# Print the shape of the DataFrame
print(components_df.shape)

# Select row 3: component
component = components_df.iloc[3]

# Print result of nlargest
print(component.nlargest())