word = "donkey"

with open("94_file.txt","r") as f:
    Text = f.read()
    
TextNew = Text.replace(word, "#####")

with open("94_file.txt","w") as f:
    Text = f.write(TextNew)