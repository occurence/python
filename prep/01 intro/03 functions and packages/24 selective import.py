"""
Selective import
General imports, like import math, make all functionality from the math package available to you. However, if you decide to only use a specific part of a package, you can always make your import more selective:

from math import pi
Try the same thing again, but this time only use pi.
"""

# Perform a selective import from the math package where you only import the pi function.
# Use pi to calculate the circumference of the circle and store it in C.
# Use pi to calculate the area of the circle and store it in A.

# Import pi function of math package
from math import pi

# Calculate C
C = 2 * 0.43 * pi

# Calculate A
A = pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))