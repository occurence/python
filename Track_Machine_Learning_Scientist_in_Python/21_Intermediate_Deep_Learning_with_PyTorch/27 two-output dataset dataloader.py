import torch
import torch.nn as nn
import pandas as pd
import numpy as np
from PIL import Image
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms

df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\21_Intermediate_Deep_Learning_with_PyTorch\datasets\omniglot_samples.csv')
samples = [
    (
        row[0],  # image path
        np.array(row[1:-1], dtype='float32'),
        int(row[-1])  # class label
    )
    for row in df.values
]

class OmniglotDataset(Dataset):
    def __init__(self, transform, samples):
		# Assign transform and samples to class attributes
        self.transform = transform
        self.samples = samples
                    
    def __len__(self):
		# Return number of samples
        return len(self.samples)

    def __getitem__(self, idx):
      	# Unpack the sample at index idx
        img_path, alphabet, label = self.samples[idx]
        img = Image.open(img_path).convert('L')
        # Transform the image 
        img_transformed = self.transform(img)
        return img_transformed, alphabet, label

# Print the sample at index 100
print(samples[100])

# Create dataset_train
dataset_train = OmniglotDataset(
    transform=transforms.Compose([
        transforms.ToTensor(),
      	transforms.Resize((64, 64)),
    ]),
    samples=samples,
)

# Create dataloader_train
dataloader_train = DataLoader(
    dataset_train, shuffle=True, batch_size=32,
)