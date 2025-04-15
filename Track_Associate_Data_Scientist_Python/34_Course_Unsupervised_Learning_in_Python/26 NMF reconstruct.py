import numpy as np

# Given feature values
nmf_features = np.array([2, 1])

# Assume components (you may have to deduce these from previous examples)
components = np.array([
    [1. , 0.5, 0. ],
    [0.2, 0.1, 2.1]
])

# Reconstruct the sample
reconstructed_sample = nmf_features @ components
print(reconstructed_sample)