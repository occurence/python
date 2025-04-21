# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
print(areas)
# Correct the bathroom area
areas[-1]=10.50
print(areas)
# Change "living room" to "chill zone"
areas[4]="chill zone"
print(areas)

print("Sweet! As the code sample showed, you can also slice a list and replace it with another list to update multiple elements in a single command.")