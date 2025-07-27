f = open("88_file.txt")
lines = f.readlines()       # f.readlines functions it means aap jitni baar run karoge utni baar aapki line read hoti jayegi. 
print(lines, type(lines))

line1 = f.readline()
print(line1, type(line1))

line2 = f.readline()
print(line2, type(line2))

line3 = f.readline()
print(line3, type(line3))

line4 = f.readline()
print(line4, type(line4))

line5 = f.readline()
print(line5, type(line5))

line6 = f.readline()
print(line6 == "")


# this code is run from while loop:

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
f.close()