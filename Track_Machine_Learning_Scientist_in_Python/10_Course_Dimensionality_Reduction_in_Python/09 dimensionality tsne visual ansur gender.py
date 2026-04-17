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

# Color the points by Gender
sns.scatterplot(x="x", y="y", hue='Gender', data=df)

# Show the plot
plt.show()

print("There is a Male and a Female cluster. t-SNE found these gender differences in body shape without being told about them explicitly! From the second plot you learned there are more males in the Combat Arms Branch.")