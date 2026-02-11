"""
Operations with other types
Variables come in different types in Python. You can see the type of a variable by using type(). For example, to see type of a, execute: type(a).

Different types behave differently in Python. When you sum two strings, for example, you'll get different behavior than when you sum two integers or two booleans.

Time for you to test this out.
"""

# Add savings and new_savings and assign it to total_savings.
# Use type() to print the resulting type of total_savings.

savings = 100
new_savings = 40

# Calculate total_savings using savings and new_savings
total_savings = savings + new_savings
print(total_savings)

# Print the type of total_savings
print(type(total_savings))

# Calculate the sum of intro and intro and assign the result to doubleintro.
# Print out doubleintro. Did you expect this?

intro = "Hello! How are you?"

# Assign sum of intro and intro to doubleintro
doubleintro = intro + intro

# Print out doubleintro
print(doubleintro)

"""
Nice. Notice how intro + intro causes "Hello! How are you?" and "Hello! How are you?" to be pasted together.
This is called concatenation. When you sum two strings, you concatenate them. The result is a new string that contains the first string followed by the second string.
"""