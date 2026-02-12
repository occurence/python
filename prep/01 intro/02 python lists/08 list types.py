"""
Create lists with different types
Although it's not really common, a list can also contain a mix of Python types including strings, floats, and booleans.

You're now going to add the room names to your list, so you can easily see both the room name and size together.

Some of the code has been provided for you to get you started. Pay attention here! "bathroom" is a string, while bath is a variable that represents the float 9.50 you specified earlier.
"""

# Finish the code that creates the areas list. Build the list so that the list first contains the name of each room as a string and then its area. In other words, add the strings "hallway", "kitchen" and "bedroom" at the appropriate locations.
# Print areas again; is the printout more informative this time?

hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)

"""
Nice! This list contains both strings and floats, but that's not a problem for Python!
"""