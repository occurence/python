import pandas as pd
import numpy as np
import re

ufo = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\11_Course_Preprocessing_for_Machine_Learning_in_Python\datasets\ufo_pattern.csv')
print(ufo[['length_of_time', 'state', 'type']].isna().sum())
ufo_no_missing = ufo.dropna(subset=['length_of_time', 'state', 'type'])
print(ufo_no_missing.shape)

def return_minutes(time_string):
    num = re.search('\d+', time_string)
    if num is not None:
        return int(num.group(0))
        
ufo["minutes"] = ufo["length_of_time"].apply(return_minutes)
print(ufo[['length_of_time','minutes']].head())
print(ufo[['seconds','minutes']].var())
ufo["seconds_log"] = np.log(ufo['seconds'])
print(ufo['seconds_log'].var())

ufo["country_enc"] = ufo["country"].apply(lambda x: 1 if x == 'us' else 0)
print(len(ufo['type'].unique()))
type_set = pd.get_dummies(ufo['type'])
ufo = pd.concat([ufo, type_set], axis=1)

print(ufo['date'].head())
ufo["month"] = pd.to_datetime(ufo["date"]).dt.month
ufo["year"] = pd.to_datetime(ufo["date"]).dt.year
print(ufo[['date','month','year']].head())

from sklearn.feature_extraction.text import TfidfVectorizer
print(ufo['desc'].head())
vec = TfidfVectorizer()
desc_tfidf = vec.fit_transform(ufo['desc'])
print(desc_tfidf.shape)

vocab = {index: word for word, index in vec.vocabulary_.items()}

def return_weights(vocab, original_vocab, vector, vector_index, top_n):
    zipped = dict(zip(vector[vector_index].indices, vector[vector_index].data))
    zipped_series = pd.Series({vocab[i]:zipped[i] for i in vector[vector_index].indices})
    zipped_index = zipped_series.sort_values(ascending=False)[:top_n].index
    return [original_vocab[i] for i in zipped_index]

def words_to_filter(vocab, original_vocab, vector, top_n):
    filter_list = []
    for i in range(0, vector.shape[0]):
        filtered = return_weights(vocab, original_vocab, vector, i, top_n)
        filter_list.extend(filtered)
    return set(filter_list)

# Make a list of features to drop
to_drop = ['city','country','lat','long','state','date','recorded','seconds','minutes','desc','length_of_time']

# Drop those features
ufo_dropped = ufo.drop(to_drop, axis=1)

# Let's also filter some words out of the text vector we created
filtered_words = words_to_filter(vocab, vec.vocabulary_, desc_tfidf, 4)