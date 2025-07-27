# a = int(input("Enter the number: "))
# b = int(input("Enter the number: "))
# c = int(input("Enter the number: "))

# average = (a + b + c)/3
# print("The average of the numbers is: ", average)


# a = int(input("Enter the number: "))
# b = int(input("Enter the number: "))                #{ #GIVE NAME FOR THIS PIECE OF                                                            of LOGIC code.
# c = int(input("Enter the number: "))                #{ #   FOR USING FUNCTIONS 
#                                                     #{ #   WE CAN SEPARATE THIS LOGIC.
# average = (a + b + c)/3                             #{
# print("The average of the numbers is: ", average)   #{

# suppose i have to do this for 50 users. then number of lines will be increases.
# so we can use loop to reduce the number of lines for using FUNCTIONS.

# USING FUNCTIONS:=

#Functions definition:---
def avg():
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    c = int(input("Enter the number: "))

    average = (a + b + c)/3
    print("The average of the numbers is: ", average)
    
#Functions call:--
avg()                # It means function ko run karo.  
avg()
avg()
avg()
avg()                #print 10 times it means i have to do this for 10 users.
avg()
avg()
avg()
avg()
avg()


