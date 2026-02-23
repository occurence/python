"""
and, or, not (2)
To see if you completely understood the boolean operators, have a look at the following piece of Python code:

x = 8
y = 9
not(not(x < 3) and not(y > 14 or y > 10))
What will the result be if you execute these three commands?

NB: Notice that not has a higher priority than and and or, it is executed first.
"""

# Possible answers

# True
# False # Correct
# Running these commands will result in an error.

# Correct! x < 3 is False. y > 14 or y > 10 is False as well. If you continue working like this, simplifying from inside outwards, you'll end up with False.