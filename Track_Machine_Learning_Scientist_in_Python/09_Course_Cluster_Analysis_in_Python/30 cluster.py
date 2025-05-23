import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans, vq

fifa = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\09_Course_Cluster_Analysis_in_Python\datasets\fifa_complete.csv')
scaled_features = ['scaled_pac','scaled_sho','scaled_pas','scaled_dri','scaled_def','scaled_phy']

# Create centroids with kmeans for 2 clusters
cluster_centers,_ = kmeans(fifa[scaled_features], 2)

# Assign cluster labels and print cluster centers
fifa['cluster_labels'], _ = vq(fifa[scaled_features], cluster_centers)
print(fifa.groupby('cluster_labels')[scaled_features].mean())

# Plot cluster centers to visualize clusters
fifa.groupby('cluster_labels')[scaled_features].mean().plot(legend=True, kind='bar')
plt.show()

# Get the name column of first 5 players in each cluster
for cluster in fifa['cluster_labels'].unique():
    print(cluster, fifa[fifa['cluster_labels'] == cluster]['name'].values[:5])