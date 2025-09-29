import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

planes = pd.read_csv(r'D:\STUDY\python\Review\11 EDA\datasets\planes.csv')

# Count the number of missing values in each column
print(planes.isna().sum())

# Find the five percent threshold
threshold = len(planes) * 0.05

# Create a filter
cols_to_drop = planes.columns[planes.isna().sum() <= threshold]

# Drop missing values for columns below the threshold
planes.dropna(subset=cols_to_drop, inplace=True)

print(planes.isna().sum())

# Check the values of the Additional_Info column
print(planes["Additional_Info"].value_counts())

# Create a box plot of Price by Airline
sns.boxplot(data=planes, x='Airline', y='Price')

plt.show()

# print(planes['Additional_Info'].isna())
# print(planes['Additional_Info'].value_counts())
# print(planes[planes['Additional_Info'].isna()])

# print(planes.loc[planes['Additional_Info'].isna(), ['Additional_Info']])
# # print(planes.value_counts())
# print(planes.loc[planes['Additional_Info'].isna(), 'Additional_Info'].value_counts(dropna=False))

# print(planes["Additional_Info"].value_counts(dropna=False))
# print(planes["Additional_Info"].value_counts())


# print(planes.loc[planes['Additional_Info'].isna(), 'Additional_Info'].value_counts(dropna=False))
# # print(planes.loc[planes['Additional_Info'].isna()])
# print(planes.loc[planes['Additional_Info'].isna(), ['Additional_Info', 'Price']])
# print(planes.loc[planes['Price'].isna(), ['Additional_Info']])
# print(planes.loc[planes['Price'].isna(), ['Additional_Info']].value_counts(dropna=False))



print(planes.loc[planes['Price'].isna()])





planes.drop(columns=['Additional_Info'], axis=1, inplace=True)

# Calculate median plane ticket prices by Airline
airline_prices = planes.groupby("Airline")["Price"].median()

print(airline_prices)

# Convert to a dictionary
prices_dict = airline_prices.to_dict()

# Map the dictionary to missing values of Price by Airline
planes["Price"] = planes["Price"].fillna(planes["Airline"].map(prices_dict))

# Check for missing values
print(planes.isna().sum())