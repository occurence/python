import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn import CrossEntropyLoss
import torch.optim as optim

input_tensor = torch.randn(1, 16)

model = nn.Sequential(
  nn.Linear(16, 8),
  nn.Linear(8, 4),
  nn.Linear(4, 2)
)

target = torch.tensor([[1., 0.]])
pred = model(input_tensor)

criterion = CrossEntropyLoss()
# loss = criterion(target.double(), one_hot_label.double())
loss = criterion(pred, target)

# Create the optimizer
optimizer = optim.SGD(model.parameters(), lr=0.001)

loss = criterion(pred, target)
loss.backward()

# Update the model's parameters using the optimizer
optimizer.step()