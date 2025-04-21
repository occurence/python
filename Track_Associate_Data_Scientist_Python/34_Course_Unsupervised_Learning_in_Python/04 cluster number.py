import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

samples = pd.read_table(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\34_Course_Unsupervised_Learning_in_Python\datasets\seeds.txt')

ks = range(1, 6)
inertias = []

for k in ks:
    # Create a KMeans instance with k clusters: model
    model = KMeans(n_clusters=k)
    
    # Fit model to samples
    model.fit(samples)
    
    # Append the inertia to the list of inertias
    inertias.append(model.inertia_)
    
# Plot ks vs inertias
plt.plot(ks, inertias, '-o')
plt.xlabel('number of clusters, k')
plt.ylabel('inertia')
plt.xticks(ks)
plt.show()