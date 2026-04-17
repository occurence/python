import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\17_Course_Introduction_to_Natural_Language_Processing\datasets\fake_or_real_news.csv', index_col=0)
train_index = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\17_Course_Introduction_to_Natural_Language_Processing\datasets\X_train_index.csv', header=None, index_col=0)
test_index = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\17_Course_Introduction_to_Natural_Language_Processing\datasets\X_test_index.csv', header=None, index_col=0)

# Import the necessary modules
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

# Print the head of df
# print(df.head())

# Create a series to store the labels: y
y = df.label

# Create training and test sets
# X_train, X_test, y_train, y_test = train_test_split(df['text'], y,test_size=0.33, random_state=53)
# X_train = df.drop(['title','label'], axis=1).iloc[train_index.index]
X_train = df.iloc[train_index.index]['text']
y_train = df[['label']].iloc[train_index.index]
y_train = y_train.values.ravel()

# X_test = df.drop(['title','label'], axis=1).iloc[test_index.index]
X_test = df.iloc[test_index.index]['text']
y_test = df[['label']].iloc[test_index.index]
y_test = y_test.values.ravel()

# Initialize a CountVectorizer object: count_vectorizer
count_vectorizer = CountVectorizer(stop_words='english')

# Transform the training data using only the 'text' column values: count_train 
count_train = count_vectorizer.fit_transform(X_train, y_train)

# Transform the test data using only the 'text' column values: count_test 
count_test = count_vectorizer.transform(X_test)

# Print the first 10 features of the count_vectorizer
print(count_vectorizer.get_feature_names_out()[:10])

# Import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize a TfidfVectorizer object: tfidf_vectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)

# Transform the training data: tfidf_train 
tfidf_train = tfidf_vectorizer.fit_transform(X_train, y_train)

# Transform the test data: tfidf_test 
tfidf_test = tfidf_vectorizer.transform(X_test)

# Print the first 10 features
print(tfidf_vectorizer.get_feature_names_out()[:10])

# Print the first 5 vectors of the tfidf training data
# print(tfidf_train.A[:5])
print(tfidf_train.toarray()[:5])

