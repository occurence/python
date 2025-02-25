import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.vq import kmeans, vq

comic_con = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\09_Course_Cluster_Analysis_in_Python\datasets\comic_con_cluster.csv')

# Import random class
from numpy import random

# Initialize seed
random.seed(0)

# Run kmeans clustering
cluster_centers, distortion = kmeans(comic_con[['x_scaled', 'y_scaled']], 2)
comic_con['cluster_labels'], distortion_list = vq(comic_con[['x_scaled', 'y_scaled']], cluster_centers)

# Plot the scatterplot
sns.scatterplot(x='x_scaled', y='y_scaled', 
                hue='cluster_labels', data = comic_con)
plt.show()