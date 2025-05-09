import pandas as pd
import torch
import torch.nn as nn
from torch.nn import CrossEntropyLoss
from torch.utils.data import DataLoader, TensorDataset

model = nn.Sequential(
    nn.Normalize(mean=[0.51378129, 0.44999619, 0.42258797], std=[0.25081163, 0.24213039, 0.24616128]),
    nn.Flatten(start_dim=1, end_dim=-1),
    nn.Linear(in_features=3072, out_features=3, bias=True)
)

# Load CSV into DataFrame
df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\20_Course_Introduction_to_Deep_Learning_with_PyTorch\datasets\validationLoader.csv')

# Example: first 2 columns are features, last 3 are labels
features = df.iloc[:, :2].values     # shape: [N, 2]
labels = df.iloc[:, 2:].values       # shape: [N, 3]

features_tensor = torch.tensor(features, dtype=torch.float32)
labels_tensor = torch.tensor(labels, dtype=torch.float32)

dataset = TensorDataset(features_tensor, labels_tensor)
validationloader = DataLoader(dataset, batch_size=32, shuffle=False)

model.eval()
validation_loss = 0.0

criterion = CrossEntropyLoss()

with torch.no_grad():
    for features, labels in validationloader:
        outputs = model(features)
        loss = criterion(outputs, labels)
        validation_loss += loss.item()
