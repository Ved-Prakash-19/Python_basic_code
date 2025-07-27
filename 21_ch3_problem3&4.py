# write a program to detect double space in a string

name = "gaurav is a good  boy"
print(name.find("  "))        #if output is -1 then not find any thing.


#replace the double space from single space in a string

name = "gaurav is a good  boy"
print(name.replace("  "," "))
print(name)  #strings are imutable which means that you cannot change them by running functions on them.