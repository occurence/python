import pandas as pd

dogs = pd.read_csv(r'D:\STUDY\python\Review\12 cat data\datasets\dogs.csv')
dogs["size"] = dogs["size"].astype("category")

# Print out the current categories of the size variable
print(dogs["size"].cat.categories)

# # Reorder the categories using the list provided
# dogs["size"] = dogs["size"].cat.reorder_categories(
#   new_categories=["small", "medium", "large"])

# Reorder the categories, specifying the Series is ordinal
dogs["size"] = dogs["size"].cat.reorder_categories(
  new_categories=["small", "medium", "large"],
  ordered=True
)

# # Reorder the categories, specifying the Series is ordinal, and overwriting the original series
# dogs["size"].cat.reorder_categories(
#   new_categories=["small", "medium", "large"],
#   ordered=True,
#   inplace=True
# )
