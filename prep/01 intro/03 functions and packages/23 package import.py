"""
Import package
Let's say you wanted to calculate the circumference and area of a circle. Here's what those formulas look like:


Rather than typing the number for pi, you can use the math package that contains the number

For reference, ** is the symbol for exponentiation. For example 3**4 is 3 to the power of 4 and will give 81.
"""

# Import the math package.
# Use math.pi to calculate the circumference of the circle and store it in C.
# Use math.pi to calculate the area of the circle and store it in A.

# Import the math package
import math

# Calculate C
C = 2 * 0.43 * math.pi

# Calculate A
A = math.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))

# Nice! If you know how to deal with functions from packages, the power of a lot of Python programmers is at your fingertips!