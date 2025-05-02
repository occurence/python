import torch
import torch.nn as nn

input_tensor = torch.Tensor([[3, 4, 6, 7, 10, 12, 2, 3, 6, 8, 9]])

# Implement a neural network with exactly four linear layers
model = nn.Sequential(
  nn.Linear(11, 1),
  nn.Linear(1, 1),
  nn.Linear(1, 1),
  nn.Linear(1, 1)
)

output = model(input_tensor)
print(output)