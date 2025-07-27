# write a program to read the text from a given file 'poem.txt' and find out whether it contains the word 'twinkle'

f = open("91_poem.txt","r")
text = f.read()
if("Twinkle in the text"):
    print("The word 'twinkle' is present  in the text")

else:
    print("The word 'twinkle' is not present in the text")
f.close()