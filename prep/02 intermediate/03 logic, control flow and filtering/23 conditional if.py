"""
if
It's time to take a closer look around in your house.

Two variables are defined in the sample code: room, a string that tells you which room of the house we're looking at, and area, the area of that room.
"""

# Examine the if statement that prints out "looking around in the kitchen." if room equals "kit".
# Write another if statement that prints out "big place!" if area is greater than 15.

# Define variables
room = "kit"
area = 14.0

# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")

# if statement for area
if area > 15:
    print("big place!")
    
# Great! big place! wasn't printed, because area > 15 is not True. Experiment with other values of room and area to see how the printouts change.