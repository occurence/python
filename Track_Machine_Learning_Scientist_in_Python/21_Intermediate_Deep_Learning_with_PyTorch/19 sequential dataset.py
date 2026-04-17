import pandas as pd
import numpy as np
import torch
from torch.utils.data import TensorDataset

def create_sequences(df, seq_length):
    xs, ys = [], []
    # Iterate over data indices
    for i in range(len(df) - seq_length):
      	# Define inputs
        x = df.iloc[i:(i+seq_length), 1]
        # Define target
        y = df.iloc[i+seq_length, 1]
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)

sequence_length = 24 * 4

train_data = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\21_Intermediate_Deep_Learning_with_PyTorch\datasets\electricity_consump\electricity_train.csv')

# Use create_sequences to create inputs and targets
X_train, y_train = create_sequences(train_data, sequence_length)
print(X_train.shape, y_train.shape)

# Create TensorDataset
dataset_train = TensorDataset(
    torch.from_numpy(X_train).float(),
    torch.from_numpy(y_train).float(),
)
print(len(dataset_train))

print("As you can see from the printed output, we have 105119 training examples, each consisting of 96 inputs and 1 target value. The TensorDataset you have just built behaves the same way as other Torch Datasets you have used before, such us our custom WaterDataset or the ImageFolder dataset; you can pass it to a DataLoader in the same way. With the sequential data ready, let's take a look at model architectures suitable for processing sequential data!")