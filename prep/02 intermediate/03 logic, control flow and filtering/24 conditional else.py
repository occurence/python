"""
Add else
In the script, the if construct for room has been extended with an else statement so that "looking around elsewhere." is printed if the condition room == "kit" evaluates to False.

Can you do a similar thing to add more functionality to the if construct for area?
"""

# Add an else statement to the second control structure so that "pretty small." is printed out if area > 15 evaluates to False.

# Define variables
room = "kit"
area = 14.0

# if-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
else :
    print("looking around elsewhere.")

# if-else construct for area
if area > 15 :
    print("big place!")
else :
    print("pretty small.")

# Nice! Again, feel free to play around with different values of room and area some more. After, head over to the next exercise where you'll take this customization one step further!