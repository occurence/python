import torch
import torch.nn as nn

torch.manual_seed(42)

input_tensor = torch.Tensor([[2, 3, 6, 7, 9, 3, 2, 1]])

# Create a container for stacking linear layers
model = nn.Sequential(nn.Linear(8, 4),
                nn.Linear(4, 1)
                )

output = model(input_tensor)
print(output)

print("Modern neural networks often span hundreds of layers. You'll review how to stack them next.")