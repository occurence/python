import re
from nltk.tokenize import regexp_tokenize

my_string = "SOLDIER #1: Found them? In Mercea? The coconut's tropical!"
pattern1 = r'(\w+|\?|!)'
pattern2 = r'(\w+|#\d|\?|!)'
pattern3 = r'(#\d\w+\?!)'
pattern4 = r'\s+'

print(regexp_tokenize(my_string, pattern1))
print(regexp_tokenize(my_string, pattern2))
print(regexp_tokenize(my_string, pattern3))
print(regexp_tokenize(my_string, pattern4))