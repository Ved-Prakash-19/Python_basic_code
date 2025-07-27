words = ["donkey", "bad", "excellent"]

with open("95_file.txt","r") as f:
    Text = f.read()

for word in words:
    Text = Text.replace(word, "#" * len(word))

with open("95_file.txt","w") as f:
    Text = f.write(Text)