from polyglot.text import Text

article = open(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\17_Course_Introduction_to_Natural_Language_Processing\datasets\french.txt', 'r', encoding='utf-8').read()
print(article)
# Create a new text object using Polyglot's Text class: txt
txt = Text(article)

# Print each of the entities found
for ent in txt.entities:
    print(ent)
    
# Print the type of ent
print(type(ent))

# Create the list of tuples: entities
entities = [(ent.tag, ' '.join(ent)) for ent in txt.entities]

# Print entities
print(entities)