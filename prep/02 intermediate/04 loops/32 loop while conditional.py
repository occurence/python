"""
Add conditionals
The while loop that corrects the offset is a good start, but what if offset is negative? You can try to run the following code where offset is initialized to -6:

# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    offset = offset - 1
    print(offset)
but your session will be disconnected. The while loop will never stop running, because offset will be further decreased on every run. offset != 0 will never become False and the while loop continues forever.

Fix things by putting an if-else statement inside the while loop.

Note that if your while loop takes too long to run, or your session is expiring, you might have created an infinite loop. In particular, remember to indent the contents of the loop using four spaces or auto-indentation, and make sure the conditions are such that the loop has a stopping point.
"""

# Initialize offset to -6.
# Inside the while loop, complete the if-else statement:
# If offset is greater than zero, you should decrease offset by 1.
# Else, you should increase offset by 1.
# If your code is taking too long to run (or your session is expiring), you probably made a mistake. Check your code and make sure that the statement offset != 0 will eventually evaluate to FALSE!

# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset -= 1
    else : 
      offset += 1    
    print(offset)

# Good work! The while loop is not that often used in Data Science, so let's head over to the for loop.