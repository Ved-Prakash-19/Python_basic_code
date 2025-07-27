with open("this.txt","r") as f:
    text = f.read()
    
with open("this_copy.txt","w") as f:
    text = f.write(text)