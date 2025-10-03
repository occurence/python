import pandas as pd

medals_won = pd.read_csv(r'D:\STUDY\python\Review\12 cat data\datasets\medals.csv', header=None)[0].tolist()

# Create a categorical Series and specify the categories (let pandas know the order matters!)
medals = pd.Categorical(medals_won, categories=['Bronze', 'Silver', 'Gold'], ordered=True)
print(medals)