import pandas as pd
import torch
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader

animals = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\20_Course_Introduction_to_Deep_Learning_with_PyTorch\datasets\animals.csv')
X = animals.iloc[:, 2:-1].to_numpy(dtype='float32')
y = animals.iloc[:, -1].to_numpy(dtype='int64')

# Create a dataset
dataset = TensorDataset(torch.tensor(X), torch.tensor(y))
# Create a DataLoader
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# Iterate over the dataloader
for batch_inputs, batch_labels in dataloader:
    print('batch_inputs:', batch_inputs)
    print('batch_labels:', batch_labels)