import pandas as pd
import matplotlib.pyplot as plt

avocados = pd.read_pickle(r'D:\STUDY\python\Review\04 dataframe inspect\avoplotto.pkl')

# Plot Bar
print(avocados.head())
nb_sold_by_size = avocados.groupby('size')['nb_sold'].sum()
nb_sold_by_size.plot(kind='bar')
plt.show()

# Plot Line
nb_sold_by_date = avocados.groupby('date')['nb_sold'].sum()
nb_sold_by_date.plot(x='date', y='nb_sold', kind='line')
plt.show()

# Plot Scatter
avocados.plot(x='nb_sold', y='avg_price', kind='scatter', title='Number of avocados sold vs. average price')
plt.show()

# Plot Histogram
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5, bins=20)
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins=20)
plt.legend(["conventional", "organic"])
plt.show()

avocados[avocados["type"] == "conventional"]["avg_price"].plot(
    kind="hist",
    bins=20,
    alpha=0.5
)
avocados[avocados["type"] == "organic"]["avg_price"].plot(
    kind="hist",
    bins=20,
    alpha=0.5
)
plt.legend(["conventional", "organic"])
plt.show()


# nb_avocados_type = avocados.groupby('type')['avg_price'].sum()
# nb_avocados_type.plot(kind='hist')
# plt.legend(["conventional", "organic"])
# plt.show()

for t in avocados["type"].unique():
    avocados[avocados["type"] == t]["avg_price"].plot(kind="hist", bins=20, alpha=0.5, label=t)

plt.legend()
plt.show()

prices_by_type = avocados.groupby("type")["avg_price"].apply(list)

for t, values in prices_by_type.items():
    plt.hist(values, bins=20, alpha=0.5, label=t)

plt.legend()
plt.show()
