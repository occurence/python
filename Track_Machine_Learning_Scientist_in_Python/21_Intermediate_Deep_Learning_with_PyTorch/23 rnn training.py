import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader
from torch.utils.data import DataLoader, TensorDataset

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        # Define lstm layer
        self.lstm = nn.LSTM(
            input_size=1,
            hidden_size=32,
            num_layers=2,
            batch_first=True,
        )
        self.fc = nn.Linear(32, 1)

    def forward(self, x):
        h0 = torch.zeros(2, x.size(0), 32)
        # Initialize long-term memory
        c0 = torch.zeros(2, x.size(0), 32)
        # Pass all inputs to lstm layer
        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        return out
    
net = Net()
# Set up MSE loss
criterion = nn.MSELoss()
optimizer = optim.Adam(
  net.parameters(), lr=0.0001
)

def create_sequences(df, seq_length):
    xs, ys = [], []
    # Iterate over data indices
    for i in range(len(df) - seq_length):
      	# Define inputs
        x = df.iloc[i:(i+seq_length), 1]
        # Define target
        y = df.iloc[i+seq_length, 1]
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)

sequence_length = 24 * 4

train_data = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\21_Intermediate_Deep_Learning_with_PyTorch\datasets\electricity_consump\electricity_train.csv')

# Use create_sequences to create inputs and targets
X_train, y_train = create_sequences(train_data, sequence_length)
print(X_train.shape, y_train.shape)

# Create TensorDataset
dataset_train = TensorDataset(
    torch.from_numpy(X_train).float(),
    torch.from_numpy(y_train).float(),
)
print(len(dataset_train))

dataloader_train = DataLoader(
  dataset_train, shuffle=True, batch_size=16
)

for epoch in range(3):
    for seqs, labels in dataloader_train:
        # Reshape model inputs
        # seqs = seqs.view(32, 96, 1)
        seqs = seqs.view(seqs.size(0), sequence_length, 1)
        # Get model outputs
        outputs = net(seqs)
        # Compute loss
        # loss = criterion(outputs, labels)
        loss = criterion(outputs, labels.view(-1, 1))
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item()}")