n = int(input("enter the number: "))

for i in range (1, n+1):
    if(i == 1 or i == n):
        print("*" * n, end="")
    
    else:
        print("*" , end="")
        print(" " * (n-2), end="")
        print("*",end = "")
    print("")
    
    
    
#  Explaination of the code:__
'''This code is printing a hollow rectangle pattern made of stars (*). The rectangle has n rows and n columns, where only the first and last rows are fully filled with stars, while the inner rows have stars at the edges and spaces in between.

Let's break it down step by step:

Getting user input:


CODE:--  n = int(input("enter the number: "))
This line takes an integer input n from the user, which will determine the size of the square (both height and width).
Loop through each row:


CODE :-- for i in range (1, n+1):
This loop runs from 1 to n. The variable i represents the current row number. Each iteration of the loop prints one row of the rectangle.
Handling the first and last rows:


CODE:--  if(i == 1 or i == n):
            print("*" * n, end="")
If the current row (i) is the first (i == 1) or the last (i == n), print n stars (*), creating a solid row of stars.
The end="" prevents the print function from moving to a new line immediately, so that the final print("") moves to the next line later.
Handling the inner rows:


else:
    print("*", end="")
    print(" " * (n-2), end="")
    print("*", end="")
For any row that's not the first or the last:
print("*", end=""): Prints a single star on the left edge of the rectangle.
print(" " * (n-2), end=""): Prints spaces in the middle. The number of spaces is (n - 2) because the stars on the left and right edges take up 2 columns.
print("*", end=""): Prints a single star on the right edge of the rectangle.
Moving to the next line:


print("")
This moves to the next line after printing each row.

Example Output (if n = 5):

*****
*   *
*   *
*   *
*****'''