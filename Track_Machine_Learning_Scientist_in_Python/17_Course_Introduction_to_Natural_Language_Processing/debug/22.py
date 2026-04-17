from polyglot.text import Text

txt = Text("Bonjour, je m'appelle Marie et j'habite à Paris.")
for ent in txt.entities:
    print(ent)
