import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import TSNE

df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\10_Course_Dimensionality_Reduction_in_Python\datasets\ansur_df.csv')
non_numeric = ['Branch', 'Gender', 'Component']
df_numeric = df.drop(non_numeric, axis=1)
m = TSNE(learning_rate=50)
tsne_features = m.fit_transform(df_numeric)
# print(tsne_features.shape)
df['x'] = tsne_features[:,0]
df['y'] = tsne_features[:,1]

# Color the points by Army Branch
sns.scatterplot(x="x", y="y", hue='Branch', data=df)

# Show the plot
plt.show()