import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

movie_plots = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\19_Course_Feature_Engineering_for_NLP_in_Python\datasets\movie_overviews.csv', index_col=0)
# movie_plots = movie_plots.fillna('')
index = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\19_Course_Feature_Engineering_for_NLP_in_Python\datasets\movie_index.csv', index_col=2, header=None)
indices = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\19_Course_Feature_Engineering_for_NLP_in_Python\datasets\movie_index.csv', header=None)
indices = indices.iloc[:, :2]
metadata = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\19_Course_Feature_Engineering_for_NLP_in_Python\datasets\metadata.csv')
# movie_plots = movie_plots.dropna()
movie_plots = movie_plots.loc[index.index, 'overview'].reset_index(drop=True)






# movie_plots = movie_plots.loc[index.index].reset_index(drop=True)
# movie_plots = movie_plots.reset_index(drop=True)
# movie_plots = movie_plots.loc[index.index, 'overview'].reset_index(drop=True)

print(movie_plots)
movie_plots.to_csv('movie_plots.csv', index=False)


# # movie_plots = movie_plots.loc[index.index]['overview']
# movie_plots = movie_plots.loc[index.index, 'overview'].reset_index(drop=True)

# def get_recommendations(title, cosine_sim, indices):
#     # Get the index of the movie that matches the title
#     idx = indices[title]
#     # Get the pairwsie similarity scores
#     sim_scores = list(enumerate(cosine_sim[idx]))
#     # Sort the movies based on the similarity scores
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#     # Get the scores for 10 most similar movies
#     sim_scores = sim_scores[1:11]
#     # Get the movie indices
#     movie_indices = [i[0] for i in sim_scores]
#     # Return the top 10 most similar movies
#     return metadata['title'].iloc[movie_indices]

# # Initialize the TfidfVectorizer 
# tfidf = TfidfVectorizer(stop_words='english')

# # Construct the TF-IDF matrix
# tfidf_matrix = tfidf.fit_transform(movie_plots)

# # Generate the cosine similarity matrix
# cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
 
# # Generate recommendations 
# print(get_recommendations('The Dark Knight Rises', cosine_sim, indices))