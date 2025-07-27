with open("this.txt","r") as f:
    text = f.read()
    
with open("renamed_by_python.txt","w") as f:
    f.write(text)

    
