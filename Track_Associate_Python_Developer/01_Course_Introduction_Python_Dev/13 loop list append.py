authors = {'Penny Jordan': 200, 'Nicholas Sparks': 22, 'Ken Follett': 30, 'Erskine Caldwell': 25, 'Wilbur Smith': 32, 'Judith Krantz': 12, 'Harold Robbins': 23, 'J. K. Rowling': 22, 'Debbie Macomber': 199, 'Eiichiro Oda': 106, 'Danielle Steel': 179, 'Barbara Cartland': 723, 'Georges Simenon': 570, 'Corín Tellado': 4000, 'Clive Cussler': 37, 'Sidney Sheldon': 21, 'Dean Koontz': 91, 'Janet Dailey': 93, 'Jirō Akagawa': 500, 'Stephen King': 77}

# Create an empty list
authors_below_twenty_five = []

# Loop through the authors dictionary
for key, value in authors.items():
  
  # Check for values less than 25
  if value < 25:
    
    # Append the author to the list
    authors_below_twenty_five.append(key)
    
print(authors_below_twenty_five)