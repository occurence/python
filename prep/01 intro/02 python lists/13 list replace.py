"""
Replace list elements
To replace list elements, you subset the list and assign new values to the subset. You can select single elements or you can change entire list slices at once.

For this and the following exercises, you'll continue working on the areas list that contains the names and areas of different rooms in a house.
"""

# Update the area of the bathroom to be 10.50 square meters instead of 9.50 using negative indexing.
# Make the areas list more trendy! Change "living room" to "chill zone". Don't use negative indexing this time.

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = 'chill zone'

# Sweet! As the code sample showed, you can also slice a list and replace it with another list to update multiple elements in a single command.