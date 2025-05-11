import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
from torchmetrics import Accuracy

class WaterDataset(Dataset):
    def __init__(self, csv_path):
        super().__init__()
        # Load data to pandas DataFrame
        df = pd.read_csv(csv_path)
        # Convert data to a NumPy array and assign to self.data
        self.data = df.to_numpy()
        
    # Implement __len__ to return the number of data samples
    def __len__(self):
        return self.data.shape[0]
    
    def __getitem__(self, idx):
        # features = self.data[idx, :-1]
        features = self.data[idx, :-1].astype('float32')
        # Assign last data column to label
        # label = self.data[idx, -1]
        label = self.data[idx, -1].astype('float32')
        return features, label
    
dataset_test = WaterDataset(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\21_Intermediate_Deep_Learning_with_PyTorch\datasets\water_test.csv')
dataloader_test = DataLoader(
    dataset_test,
    batch_size=2,
    shuffle=True,
)

# features, labels = next(iter(dataloader_test))
# print(features, labels)

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        # Define the three linear layers
        self.fc1 = nn.Linear(9, 16)
        self.fc2 = nn.Linear(16, 8)
        self.fc3 = nn.Linear(8, 1)
        
    def forward(self, x):
        # Pass x through linear layers adding activations
        x = nn.functional.relu(self.fc1(x))
        x = nn.functional.relu(self.fc2(x))
        # x = nn.functional.sigmoid(self.fc3(x))
        x = F.sigmoid(self.fc3(x))
        return x

net = Net()

# Set up binary accuracy metric
acc = Accuracy(task='binary')

net.eval()
with torch.no_grad():
    for features, labels in dataloader_test:
        # Get predicted probabilities for test data batch
        outputs = net(features)
        preds = (outputs >= 0.5).float()
        # acc(preds, labels.view(-1, 1))
        acc(preds.view(-1), labels.view(-1))

# Compute total test accuracy
test_accuracy = acc.compute()
print(f"Test accuracy: {test_accuracy}")