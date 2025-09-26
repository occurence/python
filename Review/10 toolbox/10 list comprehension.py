doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']
print([doc[0] for doc in doctor])
print([r for r in range(5)])
print([x for x in 'ABC'])
print([x for x in '24601'])
# print([x for x in 24601]) # TypeError: 'int' object is not iterable

# Create list comprehension: squares
squares = [i ** 2 for i in range(0, 10)]
print(squares)

