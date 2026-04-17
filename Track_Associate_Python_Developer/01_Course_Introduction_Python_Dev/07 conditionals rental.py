num_beds = 3
min_num_beds = 2
min_sq_foot = 750
max_rent = 1900
sq_foot = 800
rent = 1750

# Check the number of beds
print(num_beds, min_num_beds, min_sq_foot, max_rent)

if num_beds < min_num_beds:
  print("Insufficient bedrooms")

# Check square feet
elif sq_foot <= min_sq_foot:
  print("Too small")
  
# Check the rent
elif rent > max_rent:
  print("Too expensive")
  
# If all conditions met
else:
  print("This looks promising!")
