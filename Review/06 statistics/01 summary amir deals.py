import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

amir_deals = pd.read_csv(r'D:\STUDY\python\Review\06 statistics\datasets\amir_deals.csv')

# Mean and Median
deals_f = amir_deals[amir_deals['product'] == 'Product F']
print(np.mean(deals_f['amount']))
print(np.median(deals_f['amount']))

deals_a = amir_deals[amir_deals['product'] == 'Product A']
deals_a['amount'].hist()
plt.show()
print(deals_a['amount'].agg([np.mean, np.median]))

# Variance and Standard Deviation
print(amir_deals.groupby('product')['amount'].agg([np.var, np.std]))
amir_deals[amir_deals['product'] == 'Product F']['amount'].hist()
plt.show()
plt.figure()
amir_deals[amir_deals['product'] == 'Product A']['amount'].hist()
plt.show()

# Quartiles Quintiles Deciles
print(np.quantile(amir_deals['amount'], np.linspace(0, 1, 5)))
print(np.quantile(amir_deals['amount'], np.linspace(0, 1, 6)))
print(np.quantile(amir_deals['amount'], np.linspace(0, 1, 11)))

# Outliers IQR
amount_by_product= amir_deals.groupby('product')['amount'].sum()
print(amount_by_product)
q1 = np.quantile(amount_by_product, 0.25)
q3 = np.quantile(amount_by_product, 0.75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
outliers = amount_by_product[(amount_by_product < lower) | (amount_by_product > upper)]
print(outliers)

# Probability
counts = amir_deals['product'].value_counts()
probs = counts / amir_deals.shape[0]
print(probs)

# Sampling
np.random.seed(24)
sample_without_replacement = amir_deals.sample(5, replace=False)
print(sample_without_replacement)
sample_with_replacement = amir_deals.sample(5, replace=True)
print(sample_with_replacement)