with open("this.txt") as f:
    text1 = f.read()
    
with open("this_copy.txt") as f:
    text2 = f.read()
    
if(text1 == text2):
    print("yes These files are identical and matches")
    
else:
    print("no these files are not identical")