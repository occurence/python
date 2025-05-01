# Import PyTorch
import torch

temperatures = [[72, 75, 78], [70, 73, 76]]

# Create a tensor from temperatures
temp_tensor = torch.tensor(temperatures)

print(temp_tensor)
    
print("You've successfully created a tensor using temperature data. This is your first step towards building your first neural network!")