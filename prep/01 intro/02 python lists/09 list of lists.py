"""
List of lists
As a data scientist, you'll often be dealing with a lot of data, and it will make sense to group some of this data.

Instead of creating a list containing strings and floats, representing the names and areas of the rooms in your house, you can create a list of lists.

Remember: "hallway" is a string, while hall is a variable that represents the float 11.25 you specified earlier.
"""

# Finish the list of lists so that it also contains the bedroom and bathroom data. Make sure you enter these in order!
# Print out house; does this way of structuring your data make more sense?

hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)