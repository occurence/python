"""
Delete list elements
Finally, you can also remove elements from your list. You can do this with the del statement:

x = ["a", "b", "c", "d"]
del x[1]
Pay attention here: as soon as you remove an element from a list, the indexes of the elements that come after the deleted element all change!

Unfortunately, the amount you won with the lottery is not that big after all and it looks like the poolhouse isn't going to happen. You'll need to remove it from the list. You decide to remove the corresponding string and float from the areas list.
"""

# Delete the string and float for the "poolhouse" from your areas list.
# Print the updated areas list.

areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list
del areas[-4:-2]

# Print the updated list
print(areas)