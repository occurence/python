import pandas as pd
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

X_test = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\10_Course_Dimensionality_Reduction_in_Python\datasets\mnist.csv').to_numpy()

def plot_digits(data):
    fig, axes = plt.subplots(4, 4, figsize=(6, 6),
                             subplot_kw={'xticks':[], 'yticks':[]},
                             gridspec_kw=dict(hspace=0.05, wspace=0.05))
    for i, ax in enumerate(axes.flat):
        ax.imshow(data[i].reshape(28, 28),
                  cmap='binary',
                  clim=(0, 300))
    plt.show()

# Plot the MNIST sample data
plot_digits(X_test)


# pipe = Pipeline(steps=[('scaler', StandardScaler()),
#                 ('reducer', PCA(n_components=78))])
n_components = min(X_test.shape[0], X_test.shape[1])  # Ensure it's within valid range
pipe = Pipeline(steps=[('scaler', StandardScaler()),
                       ('reducer', PCA(n_components=n_components))])

# Transform the input data to principal components
# pc = pipe.transform(X_test)
pc = pipe.fit_transform(X_test)

# Prints the number of features per dataset
print(f"X_test has {X_test.shape[1]} features")
print(f"pc has {pc.shape[1]} features")