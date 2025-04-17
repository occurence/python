import pandas as pd
import re
import matplotlib.pyplot as plt
from nltk.tokenize import regexp_tokenize

with open(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\17_Course_Introduction_to_Natural_Language_Processing\datasets\grail.txt', encoding='utf-8') as f:
    holy_grail = f.read()

print(pd.DataFrame([holy_grail]))

# Split the script into lines: lines
lines = holy_grail.split('\n')

# Replace all script lines for speaker
pattern = "[A-Z]{2,}(\s)?(#\d)?([A-Z]{2,})?:"
lines = [re.sub(pattern, '', l) for l in lines]

# Tokenize each line: tokenized_lines
tokenized_lines = [regexp_tokenize(s, '\w+') for s in lines]

# Make a frequency list of lengths: line_num_words
line_num_words = [len(t_line) for t_line in tokenized_lines]

# Plot a histogram of the line lengths
plt.hist(line_num_words)

# Show the plot
plt.show()