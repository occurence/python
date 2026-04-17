genre_sales = {'Adventure': 367500000, 'Horror': 312500000, 'Literature': 80000000, 'Manga': 5166000000, 'Mystery': 300000000, 'Romance': 252500000, 'Thriller': 320000000}

# Loop through the dictionary
for genre, sale in genre_sales.items():
  
  # Check if genre is Horror or Mystery
  if genre == "Horror" or genre == "Mystery":
    print(genre, sale)