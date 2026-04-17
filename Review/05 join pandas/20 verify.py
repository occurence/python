import pandas as pd

classic_18 = pd.read_csv(r'D:\STUDY\python\Review\05 join pandas\datasets\classic_18.csv', index_col=0)
classic_19 = pd.read_csv(r'D:\STUDY\python\Review\05 join pandas\datasets\classic_19.csv', index_col=0)
pop_18 = pd.read_csv(r'D:\STUDY\python\Review\05 join pandas\datasets\pop_18.csv', index_col=0)
pop_19 = pd.read_csv(r'D:\STUDY\python\Review\05 join pandas\datasets\pop_19.csv', index_col=0)


# Concatenate the classic tables vertically
classic_18_19 = pd.concat([classic_18, classic_19], ignore_index=True)

# Concatenate the pop tables vertically
pop_18_19 = pd.concat([pop_18, pop_19], ignore_index=True)

# Merge classic_18_19 with pop_18_19
classic_pop = classic_18_19.merge(pop_18_19, on='tid')

# Using .isin(), filter classic_18_19 rows where tid is in classic_pop
popular_classic = classic_18_19[classic_18_19['tid'].isin(classic_pop['tid'])]

# Print popular chart
print(popular_classic)