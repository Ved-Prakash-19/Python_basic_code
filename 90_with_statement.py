f = open("myfile.txt")
print(f.read())
f.close()

# the same code can be written using with statement like this:-

with open("myfile.txt","r") as f:
    print(f.read())
    
# you dont have to explicitly close the file. 