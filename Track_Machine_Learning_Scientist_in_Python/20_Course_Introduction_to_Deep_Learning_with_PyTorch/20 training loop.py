import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader
from torch.nn import CrossEntropyLoss
import torch.optim as optim

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

num_epochs = 5

model = nn.Sequential(
  nn.Linear(4, 2),
  nn.Linear(2, 1)
)

optimizer = optim.SGD(model.parameters(), lr=0.001)
criterion = nn.MSELoss()

def show_results(model, dataloader):
    model.eval()
    iter_loader = iter(dataloader)
    for _ in range(3):
        feature, target = next(iter_loader)
        preds = model(feature)
        for p, t in zip(preds, target):
            print(f'Ground truth salary: {t.item():.3f}. Predicted salary: {p.item():.3f}.')

# Loop over the number of epochs and the dataloader
for i in range(num_epochs):
  for data in dataloader:
    # Set the gradients to zero
    optimizer.zero_grad()
    # Run a forward pass
    feature, target = data
    prediction = model(feature)    
    # Compute the loss
    loss = criterion(prediction, target)    
    # Compute the gradients
    loss.backward()
    # Update the model's parameters
    optimizer.step()
show_results(model, dataloader)