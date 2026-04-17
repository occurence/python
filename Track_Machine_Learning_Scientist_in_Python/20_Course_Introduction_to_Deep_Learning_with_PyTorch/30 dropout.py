import torch
import torch.nn as nn

features = torch.tensor([[-0.7739,  0.3438,  0.2899, -0.3494,  0.6050,  0.6827,  0.4756, -0.0515]])


model = nn.Sequential(
    nn.Linear(8, 6),
    nn.Linear(6, 4),
    nn.Dropout(p=0.5))

model.train()
output_train = model(features)

# Forward pass in evaluation mode (Dropout disabled)
model.eval()
output_eval = model(features)

# Print results
print("Output in train mode:", output_train)
print("Output in eval mode:", output_eval)

print("Dropout is a powerful tool against overfitting. Real-world models use hundreds of these layers to boost performance on unseen data.")