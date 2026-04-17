"""
NumPy Side Effects
numpy is great for doing vector arithmetic. If you compare its functionality with regular Python lists, however, some things have changed.

First of all, numpy arrays cannot contain elements with different types. If you mix types, like booleans and integers, numpy automatically converts them to a common type. Booleans like True and False are treated as 1 and 0 when combined with numbers, so the array ends up as integers.

Second, the typical arithmetic operators, such as +, -, * and / have a different meaning for regular Python lists and numpy arrays.

Some lines of code have been provided for you. Try these out and select the one that would match this:

np.array([True, 1, 2]) + np.array([3, 4, False])
The numpy package is already imported as np.
"""

import numpy as np

# np.array([True, 1, 2, 3, 4, False])
np.array([4, 3, 0]) + np.array([0, 2, 2])
# np.array([1, 1, 2]) + np.array([3, 4, -1])
# np.array([0, 1, 2, 3, 4, 5])

# Great job! True is converted to 1, False is converted to 0.