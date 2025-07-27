a = 'ved prakash'
b = "ved prakash"
c = '''ved prakash'''      # these three ways are correct string write in python programming.
name = "ved prakash"
nameshort = len(name)
print(nameshort)

nameshort = name[0:5]   # Here exclude 5th word name print only 0,1,2,3,4  word
print(nameshort)

nameshort = name[2:5]     # Here exclude 0 and 1st word name print only 2,3,4, word
print(nameshort)

character1 = name[4]
print(character1)

# string name if count in straight way then started with 0 and
# if count in opposite way (ending side) then started with -1 

# Negative slicing
name = "vedprakash"
print(name[-4: -1])
print(name[6:9])

name = "juhisingh"
print(name[-6:-2])
print(name[3:7])

# or other examples concept
print(name[:5])      #it means 0:5.
print(name[5:])      #it means 5:length-1.