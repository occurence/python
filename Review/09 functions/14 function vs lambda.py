powL = lambda x, y: x ** y
print(powL(2, 3))

def powF(x, y):
    return x ** y
print(powF(2, 3))

add_bangs = lambda a: a + '!!!'
print(add_bangs('hello'))


def echo_word(word1, echo):
    """Concatenate echo copies of word1."""
    words = word1 * echo
    return words

print(echo_word('hey', 5))

# Define echo_word as a lambda function: echo_word
echo_word = (lambda word1, echo: word1 * echo)

# Call echo_word: result
result = echo_word('hey', 5)

# Print result
print(result)