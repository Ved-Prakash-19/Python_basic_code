'''
for n = 3
      *
     ***
    *****
'''

'''
for n = 5
    *
   ***
  *****
 ********
**********


n = int(input("Enter the number: "))   #    This line asks the user to input a number (n). The int() converts the input into an integer.
for i in range(1, n+1):  #   Range always varied 1 to (n-1) here n tak chalana hain isliye (1, n+1).    #   This loop runs from 1 to n. The variable i represents the current row number. Each iteration of this loop creates one row of the pyramid.
    print(" " * (n-i), end="")   #   This line prints spaces (" ") before the stars to center-align the pyramid. (n - i) controls the number of spaces. As i increases (as you go down the rows), the number of spaces decreases.
    #   The end="" prevents the print function from moving to a new line, so the stars can be printed on the same line.
    print("*" * (2*i-1), end="")    #   For odd number series starting by 1.
    #   This prints the stars (*). The number of stars is controlled by the expression  (2 * i - 1) which ensures that:
    For the 1st row, 1 star is printed.
    the 2nd row, 3 stars are printed.
    For the 3rd row, 5 stars are printed, and so on.
    Again, end="" keeps the cursor on the same line for now.
    print("")    #This just moves to the next line after each row is printed.'''
    
    
    
    
n = int(input("Enter the number: "))
for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1), end="")
    print("")