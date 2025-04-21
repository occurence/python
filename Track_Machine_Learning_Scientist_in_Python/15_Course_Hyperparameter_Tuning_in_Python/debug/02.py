import pandas as pd

cc = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\15_Course_Hyperparameter_Tuning_in_Python\datasets\credit-card-full.csv')

# Try seeds from 0 to 100 (adjust range if needed)
# for seed in range(100):
#     sampled = cc.sample(1600, random_state=seed)
#     first_index = sampled.index[0]
#     print(f"Seed: {seed}, First index: {first_index}")

target_index = 21814  # Replace with the known correct index
for seed in range(100000):
    sampled = cc.sample(1600, random_state=seed)
    if sampled.index[0] == target_index:
        print(f"Found matching seed: {seed}")
        # break
