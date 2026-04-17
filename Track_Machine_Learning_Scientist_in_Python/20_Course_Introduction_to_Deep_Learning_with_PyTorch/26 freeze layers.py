import torch.nn as nn

model = nn.Sequential(
  nn.Linear(8, 16),
  nn.Linear(16, 32),
  nn.Linear(32, 10)
)

for name, param in model.named_parameters():
  
    # Check for first layer's weight
    if name == '0.weight':
   
        # Freeze this weight
        param.requires_grad = False
        
    # Check for second layer's weight
    if name == '1.weight':
      
        # Freeze this weight
        param.requires_grad = False

print("Choosing which layer to freeze is an empirical process but a good rule of thumb is to start with the first layers and go deeper.")