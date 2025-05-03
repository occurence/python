import pandas as pd
import torch
from torch.utils.data import TensorDataset

animals = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\20_Course_Introduction_to_Deep_Learning_with_PyTorch\datasets\animals.csv')
X = animals.iloc[:, 2:-1].to_numpy(dtype='float32')
y = animals.iloc[:, -1].to_numpy(dtype='int64')

# Create a dataset
dataset = TensorDataset(torch.tensor(X), torch.tensor(y))

# Print the first sample
input_sample, label_sample = dataset[0]
print('Input sample:', input_sample)
print('Label sample:', label_sample)