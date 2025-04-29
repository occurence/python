import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

transcripts = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\19_Course_Feature_Engineering_for_NLP_in_Python\datasets\transcripts.csv')
print(transcripts)
print(type(transcripts))

# # Initialize the TfidfVectorizer 
# tfidf = TfidfVectorizer(stop_words='english')

# # Construct the TF-IDF matrix
# tfidf_matrix = tfidf.fit_transform(transcripts)

# # Generate the cosine similarity matrix
# cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
 
# # Generate recommendations 
# print(get_recommendations('5 ways to kill your dreams', cosine_sim, indices))