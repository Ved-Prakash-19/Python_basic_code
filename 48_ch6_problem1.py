a1 = int(input("enter number 1:"))
a2= int(input("enter number 2:"))
a3= int(input("enter number 3:"))
a4= int(input("enter number 4:"))

if(a1>a2 and a1>a3 and a1>a4):
    print("number 1 is greatest")
elif(a2>a1 and a2>a3 and a2>a4):
    print("number 2 is greatest")
elif(a3>a1 and a3>a2 and a3>a4):
    print("number 3 is greatest")
else:
    print("number 4 is greatest")