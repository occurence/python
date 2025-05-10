import pandas as pd
import torch
import torch.nn as nn
from torch.nn import CrossEntropyLoss
import torchvision.transforms as transforms
from torchvision.datasets import CIFAR10
from torch.utils.data import DataLoader, TensorDataset

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.51378129, 0.44999619, 0.42258797],
                         std=[0.25081163, 0.24213039, 0.24616128])
])

train_dataset = CIFAR10(root='./data', train=True, download=True, transform=transform)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

model = nn.Sequential(
    nn.Flatten(start_dim=1),
    nn.Linear(3072, 3)
)

criterion = CrossEntropyLoss()

df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\20_Course_Introduction_to_Deep_Learning_with_PyTorch\datasets\validationLoader.csv')
print(df.shape)

# features = df.iloc[:, :2].values
features = df.iloc[:, :3072].values
# labels = df.iloc[:, 2:].values
# labels = df.iloc[:, 2:].values.argmax(axis=1)
labels = df.iloc[:, 3072:].values

features_tensor = torch.tensor(features, dtype=torch.float32)
# labels_tensor = torch.tensor(labels, dtype=torch.float32)
# labels_tensor = torch.tensor(labels, dtype=torch.long)
labels_tensor = torch.tensor(labels.argmax(axis=1), dtype=torch.long)

dataset = TensorDataset(features_tensor, labels_tensor)
validationloader = DataLoader(dataset, batch_size=32, shuffle=False)

# validation_dataset = CIFAR10(root='./data', train=False, download=True, transform=transform)
# validationloader = DataLoader(validation_dataset, batch_size=32, shuffle=False)


# Set the model to evaluation mode
model.eval()
validation_loss = 0.0

with torch.no_grad():
  
  for features, labels in validationloader:
    
      outputs = model(features)
      loss = criterion(outputs, labels)
      
      # Sum the current loss to the validation_loss variable
      validation_loss += loss.item()
      print(features.shape)