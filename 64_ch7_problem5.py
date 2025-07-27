n = int(input("enter a number: "))     # takes the input() as a string.
i = 1
sum = 0
while(i<=n):
    sum+=i
    i+=1
    
print("sum of this number is ",sum)



# EXPLAINATION:---

'''n = int(input("enter a number: "))

This line asks the user to input a number.
input() takes the input as a string, and int() converts it to an integer, which is stored in the variable n.

i = 1

This initializes a variable i to 1. It's going to be used to keep track of the current number in the loop.

sum = 0

A variable sum is initialized to 0. This will store the running total as we add numbers.

while(i <= n):

This is the start of a while loop. It will keep running as long as i is less than or equal to n.

sum += i

This line adds the current value of i to sum. It's a shorthand for sum = sum + i.

i += 1

This increases the value of i by 1. After each loop iteration, i will become the next number.

print(sum)

Once the loop finishes (i.e., when i becomes greater than n), the program prints the total sum of all numbers from 1 to n.


What this program does:
It asks the user to enter a number n.
It calculates the sum of all numbers from 1 to n and prints the result.
For example:

If the user enters n = 5, the program will calculate 1 + 2 + 3 + 4 + 5 and print 15.'''