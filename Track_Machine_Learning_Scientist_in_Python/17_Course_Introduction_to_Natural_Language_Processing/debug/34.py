from polyglot.text import Text

# Initialize a Text object
txt = Text("Le Monde | 10.05.2017 à 06h44 • Mis à jour le 10.05.2017 à 09h47 | Par Charles Cuvelliez")
# Access entities
for ent in txt.entities:
    print(ent)
