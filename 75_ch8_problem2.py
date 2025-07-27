# write a program using functions to convert celcius to fahrenheit.

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("enter the temp in f: "))
c = f_to_c(f)

print(f"{f_to_c(f)}°C")
print(f"{round(c,2)}°C")


#Explaination:----

def f_to_c(f):
    return 5*(f-32)/9
'''The function f_to_c(f) is defined to take one argument, f, which represents a temperature in Fahrenheit.
The formula inside the function converts Fahrenheit to Celsius using the formula:
    Celsius= 5/9 * (f-32)
    It returns the converted temperature in Celsius.'''
    
f = int(input("enter the temp in f: "))
'''The input() function prompts the user to enter a temperature in Fahrenheit.
    int() is used to convert the input string into an integer.
    The entered value is stored in the variable f.'''
    
c = f_to_c(f)
'''The function f_to_c(f) is called with the Fahrenheit temperature f entered by the user.
The result (Celsius temperature) is stored in the variable c.'''

print(f"{f_to_c(f)}°C")
'''The function f_to_c(f) is called with the Fahrenheit temperature f entered by the user.
The result (Celsius temperature) is stored in the variable c.'''

print(f"{round(c,2)}°C")
'''The function round() is used to round the Celsius temperature to 2 decimal places.'''