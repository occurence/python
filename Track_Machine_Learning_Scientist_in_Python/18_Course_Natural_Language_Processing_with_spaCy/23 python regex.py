import re

text = "Our phone number is (425)-123-4567."

# Define a pattern to match phone numbers
pattern = r"\((\d){3}\)-(\d){3}-(\d){4}"

# Find all the matching patterns in the text
phones = re.finditer(pattern, text)

# Print start and end characters and matching section of the text
for match in phones:
    start_char = match.start()
    end_char = match.end()
    print("Start character: ", start_char, "| End character: ", end_char, "| Matching text: ", text[start_char:end_char])