import torch
import torch.nn as nn
import torchvision.transforms as transforms
from torchvision.datasets import CIFAR10
from torch.utils.data import DataLoader

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

print(model)