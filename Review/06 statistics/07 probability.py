import pandas as pd

amir_deals = pd.read_csv(r'D:\STUDY\python\Review\06 statistics\datasets\amir_deals.csv')

# Count the deals for each product
counts = amir_deals['product'].value_counts()

# Calculate probability of picking a deal with each product
probs = counts / amir_deals.shape[0]
print(probs)