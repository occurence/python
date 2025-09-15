import pandas as pd

df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df2 = pd.DataFrame({"C": [5, 6], "D": [7, 8]})

# Horizontal concat
print(pd.concat([df1, df2], axis=1))

# Vertical concat
print(pd.concat([df1, df2], axis=0))
