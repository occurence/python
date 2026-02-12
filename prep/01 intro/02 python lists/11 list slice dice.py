"""
Slicing and dicing
Selecting single values from a list is just one part of the story. It's also possible to slice your list, which means selecting multiple elements from your list. Use the following syntax:

my_list[start:end]
The start index will be included, while the end index is not. However, it's also possible not to specify these indexes. If you don't specify the start index, Python figures out that you want to start your slice at the beginning of your list.
"""

# Use slicing to create a list, downstairs, that contains the first 6 elements of areas.
# Create upstairs, as the last 4 elements of areas. This time, simplify the slicing by omitting the end index.
# Print both downstairs and upstairs using print().

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[:6]

# Use slicing to create upstairs
upstairs = areas[6:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)