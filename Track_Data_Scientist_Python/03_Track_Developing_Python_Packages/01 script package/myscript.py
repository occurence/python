# Open the text file
with open(r'D:\STUDY\python\Track_Data_Scientist_Python\03_Track_Developing_Python_Packages\alice.txt') as file:
    text = file.read()

n = 0
for word in text.split():
    # Count the number of times the words in the list appear
    if word.lower() in ['cat', 'cats']:
        n += 1

print('Lewis Carroll uses the word "cat" {} times'.format(n))