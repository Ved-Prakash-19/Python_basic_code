# Q. write a program to store seven fruits in a list entered by the users?

# Initialize an empty list to store the fruits
fruits = []

 # Add the fruit to the list:--
f1 = input("enter fruits name: ")
fruits.append(f1)
f2 = input("enter fruits name: ")
fruits.append(f2)
f3 = input("enter fruits name: ")
fruits.append(f3)
f4 = input("enter fruits name: ")
fruits.append(f4)
f5 = input("enter fruits name: ")
fruits.append(f5)
f6 = input("enter fruits name: ")
fruits.append(f6)
f7 = input("enter fruits name: ")
fruits.append(f7)

print(fruits)



# blackbox ai suggestions

# Initialize an empty list to store the fruits
fruits = []

# Loop to get input from the user seven times
for i in range(7):
    # Get the fruit name from the user
    fruit = input("Enter fruit #{}: ".format(i+1))
    
    # Add the fruit to the list
    fruits.append(fruit)

# Print the list of fruits
print("You entered the following fruits:")
for fruit in fruits:
    print(fruit)

