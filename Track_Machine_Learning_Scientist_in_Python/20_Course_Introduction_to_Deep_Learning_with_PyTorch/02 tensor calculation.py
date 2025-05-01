import torch

temperatures = torch.tensor([[72, 75, 78], [70, 73, 76]])
adjustment = torch.tensor([[2, 2, 2], [2, 2, 2]])

# Display the shape of the adjustment tensor
print("Adjustment shape:", adjustment.shape)

# Display the type of the adjustment tensor
print("Adjustment type:", adjustment.dtype)

print("Temperatures shape:", temperatures.shape)
print("Temperatures type:", temperatures.dtype)

# Add the temperatures and adjustment tensors
corrected_temperatures = adjustment + temperatures
print("Corrected temperatures:", corrected_temperatures)

print("You've verified the tensors and adjusted the temperature data. Next, let’s learn the role of tensors within neural networks.")