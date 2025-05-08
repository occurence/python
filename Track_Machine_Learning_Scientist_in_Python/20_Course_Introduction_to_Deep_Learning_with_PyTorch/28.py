import pandas as pd
import torch
import torch.nn as nn

# model = nn.Sequential(
#     nn.Normalize(mean=[0.51378129, 0.44999619, 0.42258797], std=[0.25081163, 0.24213039, 0.24616128]),
#     nn.Flatten(start_dim=1, end_dim=-1),
#     nn.Linear(in_features=3072, out_features=3, bias=True)
# )

test = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\20_Course_Introduction_to_Deep_Learning_with_PyTorch\datasets\validationLoader.csv')

print(test)