a = int(input("enter your age"))

# IF statement no:1:---

if(a%2 == 0):
    print("a is even")       #this if statement is independent.
        #END of if statement no:1
        
#IF statement no:2:--
if(a>=18):
    print("you are adult")

elif(a==0):
    print("you are entering an age which is not valid")    #this if statement is dependent on the previous one.
elif(a<0):
    print("you are entering an invalid age")
    
else:
    print("you are a minor")   #this if statement is dependent on the previous one.
    #END of if statement no:-2
    
    print("end of program")