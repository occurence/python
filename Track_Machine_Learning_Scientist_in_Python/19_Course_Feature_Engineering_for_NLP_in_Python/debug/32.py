import pandas as pd

# Load both datasets
movie_plots = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\19_Course_Feature_Engineering_for_NLP_in_Python\datasets\movie_overviews.csv', index_col=0)
index = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\19_Course_Feature_Engineering_for_NLP_in_Python\datasets\movie_index.csv', index_col=2, header=None)

# Loop over the index DataFrame and print overviews
for idx in index.index:
    try:
        print(movie_plots.loc[49026]['overview'])
    except KeyError:
        print(f"Index {49026} not found in movie_plots.")
