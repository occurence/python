import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.vq import kmeans

uniform_data = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\09_Course_Cluster_Analysis_in_Python\datasets\uniform_data.csv')

distortions = []
num_clusters = range(2, 7)

# Create a list of distortions from the kmeans function
for i in num_clusters:
    cluster_centers, distortion = kmeans(uniform_data[['x_scaled', 'y_scaled']], i)
    distortions.append(distortion)

# Create a DataFrame with two lists - number of clusters and distortions
elbow_plot = pd.DataFrame({'num_clusters': num_clusters, 'distortions': distortions})

# Creat a line plot of num_clusters and distortions
sns.lineplot(x='num_clusters', y='distortions', data=elbow_plot)
plt.xticks(num_clusters)
plt.show()

print("There is no well defined elbow in this plot!")