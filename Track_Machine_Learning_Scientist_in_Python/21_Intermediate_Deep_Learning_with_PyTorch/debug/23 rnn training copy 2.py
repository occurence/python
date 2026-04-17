import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader
from torchvision import transforms
from torch.utils.data import DataLoader, TensorDataset
from sklearn.preprocessing import StandardScaler

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 20, 5)
        self.conv2 = nn.Conv2d(20, 20, 5)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        return F.relu(self.conv2(x))

net = Net()
# Set up MSE loss
criterion = nn.MSELoss()
optimizer = optim.Adam(
  net.parameters(), lr=0.0001
)

# Define transforms
train_transforms = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(45),
    transforms.RandomAutocontrast(),
    transforms.ToTensor(),
    transforms.Resize((64, 64)),
])

# dataset_train = ImageFolder(
#   r"D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\21_Intermediate_Deep_Learning_with_PyTorch\datasets\clouds\clouds\clouds_train",
#   transform=train_transforms,
# )
# dataloader_train = DataLoader(
#   dataset_train, shuffle=True, batch_size=16
# )

df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\21_Intermediate_Deep_Learning_with_PyTorch\datasets\electricity_consump\electricity_train.csv', parse_dates=['timestamp'])
consumption = df['consumption'].values.reshape(-1, 1)
window_size = 96
batch_size = 16

# X = df.iloc[:, :-1].values
# y = df.iloc[:, -1].values
scaler = StandardScaler()
consumption_scaled = scaler.fit_transform(consumption)
# X_scaled = scaler.fit_transform(X)
X = []
y = []
for i in range(len(consumption_scaled) - window_size):
    X.append(consumption_scaled[i:i + window_size])
    y.append(consumption_scaled[i + window_size])

X_tensor = torch.tensor(X, dtype=torch.float32)
y_tensor = torch.tensor(y, dtype=torch.float32)

dataset_train = TensorDataset(X_tensor, y_tensor)
dataloader_train = DataLoader(dataset_train, shuffle=True, batch_size=batch_size)

for epoch in range(3):
    for seqs, labels in dataloader_train:
        # Reshape model inputs
        # seqs = seqs.view(32, 96, 1)
        seqs = seqs.view(seqs.size(0), 96, 1)
        # Get model outputs
        outputs = net(seqs)
        # Compute loss
        loss = criterion(outputs, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item()}")