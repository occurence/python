# Open "alice.txt" and assign the file to "file"
with open(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\24_Course_Writing_Functions_in_Python\datasets\alice.txt', encoding='utf-8') as file:
  text = file.read()

n = 0
for word in text.split():
  if word.lower() in ['cat', 'cats']:
    n += 1

print('Lewis Carroll uses the word "cat" {} times'.format(n))